from django import template

register = template.Library()


@register.filter(is_safe=False)
def token_transfers(token_transfers):

    if not token_transfers: return token_transfers
    for token_transfer in token_transfers:
        amount = token_transfer['amount']
        currency_decimals = token_transfer['currency_decimals']
        usdDayPrice = token_transfer['usdDayPrice']
        if currency_decimals == 0:
            formatted_amount = amount
        else:
            formatted_amount = round(amount / (10 ** currency_decimals), 3)

        token_transfer['formatted_amount'] = formatted_amount

        if usdDayPrice:
            formatted_usd_amount = round(formatted_amount * float(usdDayPrice), 2)
            token_transfer['amount_usd'] = formatted_usd_amount

    return token_transfers
