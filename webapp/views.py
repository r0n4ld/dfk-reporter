from pyhmy import account
from django.conf import settings
from annoying.decorators import render_to
from web3.exceptions import TransactionNotFound
from .dfk_contracts import mastergardener, meditationcircle, auction, quest, summoning, wishingwell, wone, uniswapv2router, bank, profile, erc20
from web3.logs import DISCARD
from .models import Token
import requests
import datetime

from .utils import convert_one_to_hex
from .models import CHAIN_HARMONY_ONE
from web3 import Web3

JEWEL_TOKEN_ADDRESS = '0x72Cb10C6bfA5624dD07Ef608027E366bd690048F'
AIRDROP = '0xa678d193fEcC677e137a00FEFb43a9ccffA53210'


def get_erc20_transfers_for_wallet(timestamp, receipt, wallet, chain=CHAIN_HARMONY_ONE):
    internal_receipt = erc20.CONTRACT.events.Transfer().processReceipt(receipt, errors=DISCARD)
    r_in = []
    r_out = []
    for item in internal_receipt:
        r_from = item['args']['from']
        r_to = item['args']['to']
        r_value = item['args']['value']
        r_token = item['address']

        token = Token.objects.filter(chain=chain, address__iexact=r_token).first()
        if token:
            currency_name = token.name
            currency_decimals = token.decimals
        else:
            w3 = Web3(Web3.HTTPProvider(settings.RPC_ADDRESS))
            from .abi import simple_abi
            token_contract = w3.eth.contract(Web3.toChecksumAddress(r_token), abi=simple_abi)
            token = Token()
            token.chain = CHAIN_HARMONY_ONE
            token.address = Web3.toChecksumAddress(r_token)
            token.decimals = token_contract.functions.decimals().call()
            token.name = token_contract.functions.name().call()
            token.symbol = token_contract.functions.symbol().call()
            token.save()
            currency_name = token.name
            currency_decimals = token.decimals

        usdDayPrice = TokenPrice.objects.filter(address=token.address, datetime__date=timestamp.date()).first()
        usdDayPrice = usdDayPrice.price if usdDayPrice else None

        # Transaction sent FROM wallet TO another wallet
        if r_from == wallet and r_to != wallet:
            existing_item_out = next((x for x in r_out if x['currency'] == r_token), None)
            existing_item_in = next((x for x in r_in if x['currency'] == r_token), None)

            if existing_item_out:
                existing_item_out['amount'] += r_value
                r_value = 0

            elif existing_item_in:
                if r_value >= existing_item_in['amount']:  # value going out is bigger than value coming in.
                    r_value -= existing_item_in['amount']
                    r_in.remove(existing_item_in)
                else:  # value going out is less than coming in
                    existing_item_in['amount'] -= r_value
                    r_value = 0

            if r_value:
               item_out = {'amount': r_value, 'currency': r_token, 'currency_name': currency_name, 'currency_decimals': currency_decimals, 'usdDayPrice': usdDayPrice, 'tokenUsd': 1}
               r_out.append(item_out)

        # Transaction sent TO wallet FROM another wallet
        elif r_to == wallet and r_from != wallet:
            existing_item_out = next((x for x in r_out if x['currency'] == r_token), None)
            existing_item_in = next((x for x in r_in if x['currency'] == r_token), None)

            if existing_item_in:
                existing_item_in['amount'] += r_value
                r_value = 0

            elif existing_item_out:
                if r_value >= existing_item_out['amount']:  # value coming in is bigger than value going out
                    r_value -= existing_item_out['amount']
                    r_in.remove(existing_item_out)
                else:  # value coming in is less than going out
                    existing_item_out['amount'] -= r_value
                    r_value = 0

            if r_value:
               item_in = {'amount': r_value, 'currency': r_token, 'currency_name': currency_name, 'currency_decimals': currency_decimals, 'usdDayPrice': usdDayPrice}
               r_in.append(item_in)

        else:
            # either to same wallet or between other wallets
            pass
    return r_in, r_out


from .models import TokenPrice
from pycoingecko import CoinGeckoAPI


headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0'
}


@render_to('dfk.html')
def index(request):
    has_next_page = False

    # Handle form input
    wallet = request.POST.get('wallet', '')
    wallet_one = ''
    error = ''
    if wallet.startswith('one'):
        wallet_one = wallet
        try:
            wallet = convert_one_to_hex(wallet)
        except ValueError:
            wallet = ''
            error = 'Wallet is not valid.'
    elif wallet:
        wallet_one = ''
        try:
            wallet = Web3.toChecksumAddress(wallet)
        except Exception:
            error = 'Wallet is not valid.'
            wallet = ''
    if not wallet:
        return {'error': error}

    # Page
    page = request.POST.get('page', '')
    if page.isdigit():
        page = int(page)
    else:
        page = 0

    # Only tranfers
    if request.POST.get('only_transfers'):
        only_transfers = request.POST.get('only_transfers') == 'on'
    else:
        only_transfers = True

    w3 = Web3(Web3.HTTPProvider(settings.RPC_ADDRESS))

    profile_name = profile.get_profile_name(wallet)

    transactions = account.get_transaction_history(wallet, page=page, page_size=1000, include_full_tx=True, endpoint=settings.RPC_ADDRESS, order="ASC")
    transactions.sort(key=lambda t: int(t['timestamp'], 16))
    if len(transactions) == 1000:
        has_next_page = True

    dfk_transactions = []
    heroes_questlog = {}
    for transaction in transactions:
        dfk_transaction = {'tx': transaction}
        dfk_location = 'unknown'
        dfk_npc = ''
        dfk_action = 'unknown'
        dfk_info = ""
        dfk_transaction['timestamp'] = datetime.datetime.utcfromtimestamp(int(transaction['timestamp'], 16))

        tx_to = convert_one_to_hex(transaction['to'])
        tx_from = convert_one_to_hex(transaction['from'])

        # Do a quick filter on DFK contracts/transfers
        cont = tx_to in [wallet, AIRDROP, bank.CONTRACT_ADDRESS, mastergardener.CONTRACT_ADDRESS, profile.CONTRACT_ADDRESS, uniswapv2router.CONTRACT_ADDRESS,
                         auction.CONTRACT_ADDRESS, quest.CONTRACT_ADDRESS, summoning.CONTRACT_ADDRESS, meditationcircle.CONTRACT_ADDRESS]
        if not cont:
            continue

        try:
            transaction_receipt = w3.eth.getTransactionReceipt(transaction['hash'])
        except TransactionNotFound as e:
            print(e)
            continue

        # Skip failed transactions
        if transaction_receipt['status'] != 1:
            continue

        tokens_in, tokens_out = get_erc20_transfers_for_wallet(dfk_transaction['timestamp'], transaction_receipt, wallet)

        internal_receipt = wone.CONTRACT.events.Deposit().processReceipt(transaction_receipt, errors=DISCARD)
        for item in internal_receipt:
            amount = item['args']['wad']

            usdDayPrice = TokenPrice.objects.filter(token='ONE', datetime__date=dfk_transaction['timestamp'].date()).first().price
            tokens_out.append({'amount': amount, 'currency': '0x', 'currency_name': 'ONE', 'currency_decimals': 18, 'usdDayPrice': usdDayPrice})

        internal_receipt = wone.CONTRACT.events.Withdrawal().processReceipt(transaction_receipt, errors=DISCARD)
        for item in internal_receipt:
            amount = item['args']['wad']

            usdDayPrice = TokenPrice.objects.filter(token='ONE', datetime__date=dfk_transaction['timestamp'].date()).first().price
            tokens_in.append({'amount': amount, 'currency': '0x', 'currency_name': 'ONE', 'currency_decimals': 18, 'usdDayPrice': usdDayPrice})

        if tx_to == wallet and transaction['input'] == '0x':
            dfk_location = 'Non DFK'
            dfk_action = 'receiveTokens'
            dfk_info = "Received ONE from another wallet"

            usdDayPrice = TokenPrice.objects.filter(token='ONE', datetime__date=dfk_transaction['timestamp'].date()).first().price

            tokens_in.append({'amount': int(transaction['value'], 16), 'currency': '0x', 'currency_name': 'ONE', 'currency_decimals': 18, 'usdDayPrice': usdDayPrice})

        if only_transfers and not tokens_in and not tokens_out and tx_to not in [auction.CONTRACT_ADDRESS, summoning.CONTRACT_ADDRESS, quest.CONTRACT_ADDRESS]:
            continue

        # Airdrop
        elif tx_to == AIRDROP:
            # Example wallet: 0x6e198cb7479c42e082ace9db678306356050070f
            dfk_location = 'Airdrop'
            dfk_action = 'Airdrop'
            dfk_info = "Received from airdrop"

        # Bank
        elif tx_to == bank.CONTRACT_ADDRESS:
            dfk_location = 'Bank'
            dfk_npc = 'Teller'
            func_obj, func_params = bank.CONTRACT.decode_function_input(transaction["input"])
            dfk_action = func_obj.abi['name']
            if func_obj.abi['name'] == 'enter':
                dfk_info = "Deposit tokens into Bank"

            elif func_obj.abi['name'] == 'leave':
                dfk_info = "Withdraw tokens from Bank"
            else:
                print(f'{transaction["hash"]}: BANK UNKNOWN')

        # Banker
        elif tx_to == '0x3685Ec75Ea531424Bbe67dB11e07013ABeB95f1e':  # banker
            dfk_location = 'Bank'
            dfk_info = "Claim bank rewards"
            print(f"{transaction['hash']}: banker")

        # Mastergardener
        elif tx_to == mastergardener.CONTRACT_ADDRESS:
            dfk_location = 'Gardens'
            dfk_npc = 'Seed Box'
            func_obj, func_params = mastergardener.CONTRACT.decode_function_input(transaction["input"])
            dfk_action = func_obj.abi['name']
            if func_obj.abi['name'] == 'deposit':
                dfk_info = "Deposit LP Tokens"

            elif func_obj.abi['name'] == 'claimReward' or func_obj.abi['name'] == 'claimRewards':
                dfk_taxable_event = True
                # special case. Contracts adds all tokens to wallet then removes locked tokens.
                dfk_info = "Claim garden rewards (not showing locked Jewels)"

            elif func_obj.abi['name'] == 'withdraw':
                dfk_info = "Withdraw LP Tokens (not showing locked Jewels)"
            else:
                dfk_info = f'mastergardener UNKNOWN {func_obj}'

        # Profile
        elif tx_to == profile.CONTRACT_ADDRESS:
            dfk_location = 'Profile'
            dfk_info = 'Configure profile'

        # uniswapv2router
        elif tx_to == uniswapv2router.CONTRACT_ADDRESS:

            dfk_location = 'Marketplace'
            func_obj, func_params = uniswapv2router.CONTRACT.decode_function_input(transaction["input"])

            dfk_action = func_obj.abi['name']

            if dfk_action in ['swapTokensForExactTokens', 'swapETHForExactTokens', 'swapExactETHForTokens', 'swapExactTokensForETH', 'swapExactTokensForTokens']:
                dfk_npc = 'Trader'
                dfk_info = "Swap tokens"

            elif dfk_action in ['addLiquidityETH', 'addLiquidity']:
                dfk_npc = 'Druid'
                dfk_info = "Buy liquidity tokens"

            elif dfk_action in ['removeLiquidity', 'removeLiquidityETH']:
                dfk_npc = 'Druid'
                dfk_info = "Sell liquidity tokens"

        # Summoning
        elif tx_to == summoning.CONTRACT_ADDRESS:
            func_obj, func_params = summoning.CONTRACT.decode_function_input(transaction["input"])
            if str(func_obj) == '<Function cancelAuction(uint256)>':
                dfk_location = 'Tavern'
                dfk_npc = 'Agent'
                heroId = func_params['_tokenId']
                dfk_info = f'Cancel list hero {heroId} for hire'
            elif str(func_obj) == '<Function createAuction(uint256,uint128,uint128,uint64,address)>':
                dfk_location = 'Tavern'
                dfk_npc = 'Agent'
                dfk_info = f'List hero {heroId} for hire'

                receipt_result = summoning.CONTRACT.events.AuctionCreated().processReceipt(transaction_receipt, errors=DISCARD)
                for i in receipt_result:
                    heroId = func_params["_tokenId"]
                    query = """
                        query ($id: Int) { 
                            assistingAuction (id: $id) {
                                open
                                purchasePrice
                            }
                        }  
                    """
                    variables = {
                        "id": i["args"]["auctionId"],
                    }
                    urlAuctionHouse = "http://graph3.defikingdoms.com/subgraphs/name/defikingdoms/apiv5"
                    r = requests.post(urlAuctionHouse, json={'query': query, "variables": variables}, headers=headers)

                    if str(r.json()["data"]["assistingAuction"]) == "None":
                        dfk_info = f"List hero {heroId} for hire"
                    elif str(r.json()["data"]["assistingAuction"]["open"]) == "True":
                        dfk_info = f"List hero {heroId} for hire"
                    elif str(r.json()["data"]["assistingAuction"]["purchasePrice"]) == "None":
                        dfk_info = f"List hero {heroId} for hire"
                    else:
                        dfk_info = f"Hired out hero {heroId}"
                        tokens_in.append(
                            {'amount': func_params["_startingPrice"], 'currency': JEWEL_TOKEN_ADDRESS, 'currency_name': 'Jewel', 'currency_decimals': 18, 'usdDayPrice': None})

            elif str(func_obj) == '<Function summonCrystal(uint256,uint256,uint16,uint16,address)>':
                dfk_location = 'Portal'
                dfk_npc = 'Arch druid'
                dfk_info = "Summon crystal"

            elif str(func_obj) == '<Function open(uint256)>':
                dfk_location = 'Portal'
                dfk_npc = 'Arch druid'
                receipt_result = summoning.CONTRACT.events.CrystalOpen().processReceipt(transaction_receipt)
                heroId = receipt_result[0]['args']['heroId']
                dfk_info = f'Open Crystal containing hero {heroId}'

            else:
                dfk_location = 'Portal'
                dfk_npc = 'Arch druid'
                dfk_info = str(func_obj)

            if only_transfers and not tokens_in:
                continue

        # Tavern
        elif tx_to == auction.CONTRACT_ADDRESS:
            # Examples of buying/selling on 0x36f217187cb802f85fa20d6882a3b6ab579df437
            dfk_location = 'Tavern'
            dfk_npc = 'Agent'
            try:
                func_obj, func_params = auction.CONTRACT.decode_function_input(transaction["input"])
            except Exception as e:
                print(e)
            else:
                dfk_action = func_obj.abi['name']
                if dfk_action == 'bid':
                    dfk_info = f"Bought hero {func_params['_tokenId']}"
                elif dfk_action == 'createAuction':
                    dfk_info = 'Created auction'

                    receipt_result = auction.CONTRACT.events.AuctionCreated().processReceipt(transaction_receipt, errors=DISCARD)
                    for i in receipt_result:
                        heroId = func_params["_tokenId"]
                        query = """
                            query ($id: Int) { 
                                saleAuction (id: $id) {
                                    open
                                    purchasePrice
                                    endedAt
                                }
                            }  
                        """
                        variables = {
                            "id": i["args"]["auctionId"],
                        }
                        urlAuctionHouse = "http://graph3.defikingdoms.com/subgraphs/name/defikingdoms/apiv5"
                        r = requests.post(urlAuctionHouse, json={'query': query, "variables": variables}, headers=headers)
                        r_json = r.json()
                        if str(r_json["data"]["saleAuction"]) == "None":
                            dfk_info = f"List hero {heroId} for sale"
                        elif str(r_json["data"]["saleAuction"]["open"]) == "True":
                            dfk_info = f"List hero {heroId} for sale"
                        elif str(r_json["data"]["saleAuction"]["purchasePrice"]) == "None":
                            dfk_info = f"List hero {heroId} for sale"
                        else:
                            dfk_info = f"Sold hero {heroId}"
                            endedAt = datetime.datetime.fromtimestamp(int(r_json['data']['saleAuction']['endedAt']))
                            usdDayPrice = TokenPrice.objects.filter(address=JEWEL_TOKEN_ADDRESS, datetime__date=endedAt.date()).first()
                            tokens_in.append({'amount': func_params["_startingPrice"], 'currency': JEWEL_TOKEN_ADDRESS, 'currency_name': 'Jewel', 'currency_decimals': 18, 'usdDayPrice': usdDayPrice.price if usdDayPrice else None})

                elif dfk_action == 'cancelAuction':
                    heroId = func_params["_tokenId"]
                    dfk_info = f'Cancelled auction for hero {heroId}'
                else:
                    dfk_info = dfk_action

            if only_transfers and not tokens_in and dfk_action != 'bid':
                continue

        # Quest
        elif tx_to == quest.CONTRACT_ADDRESS:
            dfk_location = 'Professions'
            try:
                func_obj, func_params = quest.CONTRACT.decode_function_input(transaction["input"])
            except Exception as e:
                dfk_info = f"Unknown quest"

            else:
                dfk_action = func_obj.abi['name']
                if dfk_action == 'completeQuest':
                    heroesIds = set()
                    receipt_result = quest.CONTRACT.events.QuestReward().processReceipt(transaction_receipt, errors=DISCARD)
                    for r in receipt_result:
                        heroesIds.add(r["args"]["heroId"])

                    heroesIds = list(heroesIds)
                    heroesIds.sort()
                    heroes = ", ".join([str(s) for s in heroesIds])
                    try:
                        dfk_npc = heroes_questlog.pop(heroes)
                    except KeyError:
                        pass

                    dfk_info = f"Completed quest for hero(es) {heroes}"

                elif dfk_action in ['startQuest', 'startQuestWithData']:
                    # func_params = {'_heroIds': [13611], '_questAddress': '0x3132c76acF2217646fB8391918D28a16bD8A8Ef4', '_attempts': 3}
                    heroesIds = func_params['_heroIds']
                    heroesIds.sort()
                    heroes = ", ".join([str(s) for s in heroesIds])
                    quest_address = func_params['_questAddress']
                    if quest_address == '0xE259e8386d38467f0E7fFEdB69c3c9C935dfaeFc':
                        dfk_npc = 'Fisher'
                    elif quest_address == '0x3132c76acF2217646fB8391918D28a16bD8A8Ef4':
                        dfk_npc = 'Forager'
                    elif quest_address == '0x569E6a4c2e3aF31B337Be00657B4C040C828Dd73':
                        dfk_npc = 'Miner'
                    elif quest_address == '0x0548214A0760a897aF53656F4b69DbAD688D8f29':
                        dfk_npc = 'Wishing well'
                    elif quest_address == '0xe4154B6E5D240507F9699C730a496790A722DF19':
                        dfk_npc = 'Gardener'
                    elif quest_address == '0x6FF019415Ee105aCF2Ac52483A33F5B43eaDB8d0':
                        dfk_npc = 'Miner'
                    else:
                        dfk_npc = quest_address
                    dfk_info = f"Start quest for hero(es) {heroes}"
                    heroes_questlog[heroes] = dfk_npc

                elif dfk_action == 'cancelQuest':
                    dfk_info = "Cancel quest"

            if only_transfers and not tokens_in:
                continue

        # Wishing well
        elif tx_to == wishingwell.CONTRACT_ADDRESS:
            dfk_location = 'Wishing Well'

        # Meditation circle
        elif tx_to == meditationcircle.CONTRACT_ADDRESS:
            dfk_location = 'Meditation Circle'
            dfk_npc = 'Wanderer'

            func_obj, func_params = meditationcircle.CONTRACT.decode_function_input(transaction["input"])
            dfk_action = func_obj.abi['name']
            if dfk_action == 'startMeditation':
                hero = func_params['_heroId']
                dfk_info = f"Start meditation for hero {hero}"

            elif dfk_action == 'completeMeditation':
                hero = func_params['_heroId']
                dfk_info = f"Completed meditation for hero {hero}"
                pass

        dfk_transaction['location'] = dfk_location
        dfk_transaction['npc'] = dfk_npc
        dfk_transaction['action'] = dfk_action
        dfk_transaction['info'] = dfk_info
        dfk_transaction['tokens_in'] = tokens_in
        dfk_transaction['tokens_out'] = tokens_out
        dfk_transactions.append(dfk_transaction)

    return {'dfk_transactions': dfk_transactions, 'profile_name': profile_name, 'wallet': wallet, 'wallet_one': wallet_one, 'has_next_page': has_next_page, 'error': error, 'only_transfers': only_transfers, 'next_page': page+1}


@render_to('empty.html')
def update(request):
    # Start with data from DFK itself.
    query = """
{
  tokens(first: 1000, where: {tradeVolume_gt: 0}) {
    id
    symbol
    tokenDayData(first: 1000, orderDirection: asc, where:{priceUSD_lt:1000000000}) {
      date
      priceUSD
    }
  }
}
    """
    dexUrl = 'https://graph4.defikingdoms.com/subgraphs/name/defikingdoms/dex'
    result = requests.post(dexUrl, json={'query': query, 'variables': {}}, headers=headers)
    result_json = result.json()
    for token in result_json['data']['tokens']:
        for price in token['tokenDayData']:
            d = price['date']
            priceUSD = price['priceUSD']
            TokenPrice.objects.get_or_create(token=token['symbol'], address=Web3.toChecksumAddress(token['id']), datetime=datetime.datetime.utcfromtimestamp(d), defaults={'price': priceUSD})

    # LP Pair data from DFK against Jewel pair
    for t in ['token0', 'token1']:
        query = """
            {
              pairs(first:1000, where: {%s: "0x72cb10c6bfa5624dd07ef608027e366bd690048f"}) {
                id
                token0 {
                  name
                  id
                }
                token1 {
                  name
                  id
                }
              }
            }
        """ % t
        result = requests.post(dexUrl, json={'query': query, 'variables': {}}, headers=headers)
        result_json = result.json()
        for item in result_json['data']['pairs']:
            import decimal
            query = """
            {
              pairDayDatas(first: 1000, where: {pairAddress: "%s"}) {
                token0 {
                  name
                }
                token1 {
                  name
                }
                date
                pairAddress
                totalSupply
                reserveUSD
              }
            } 
                """ % (item['id'])
            result = requests.post(dexUrl, json={'query': query, 'variables': {}}, headers=headers)
            result_json = result.json()
            for item in result_json['data']['pairDayDatas']:
                if float(item['totalSupply']) <= 0: continue
                d = item['date']
                priceUSD = float(item['reserveUSD']) / float(item['totalSupply'])
                name = item['token0']['name'] + " - " + item['token1']['name'] + " LP"
                try:
                    TokenPrice.objects.get_or_create(token=name, address=Web3.toChecksumAddress(item['pairAddress']), datetime=datetime.datetime.utcfromtimestamp(d), defaults={'price': priceUSD})
                except decimal.InvalidOperation:
                    pass

    # For whatever data we did not get yet, update with data from CoinGecko.
    cg = CoinGeckoAPI()
    prices = cg.get_coin_market_chart_range_by_id("harmony", "usd", 1629496800, datetime.datetime.timestamp(datetime.datetime.now()))
    for line in prices['prices']:
        TokenPrice.objects.get_or_create(token='ONE', address='0x', datetime=datetime.datetime.utcfromtimestamp(line[0]/1000), defaults={'price': line[1]})

    prices = cg.get_coin_market_chart_range_by_id("defi-kingdoms", "usd", 1629496800, datetime.datetime.timestamp(datetime.datetime.now()))
    for line in prices['prices']:
        TokenPrice.objects.get_or_create(token='JEWEL', address=JEWEL_TOKEN_ADDRESS, datetime=datetime.datetime.utcfromtimestamp(line[0]/1000), defaults={'price': line[1]})

    return {}
