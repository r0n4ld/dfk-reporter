from django.conf import settings
from web3 import Web3

CONTRACT_ADDRESS = '0x65DEA93f7b886c33A78c10343267DD39727778c2'

ABI = [
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "auctionId",
          "type": "uint256"
        },
        {
          "indexed": True,
          "internalType": "uint256",
          "name": "tokenId",
          "type": "uint256"
        }
      ],
      "name": "AuctionCancelled",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "auctionId",
          "type": "uint256"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "uint256",
          "name": "tokenId",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "startingPrice",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "endingPrice",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "duration",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "winner",
          "type": "address"
        }
      ],
      "name": "AuctionCreated",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "auctionId",
          "type": "uint256"
        },
        {
          "indexed": True,
          "internalType": "uint256",
          "name": "tokenId",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "totalPrice",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "winner",
          "type": "address"
        }
      ],
      "name": "AuctionSuccessful",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "crystalId",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "heroId",
          "type": "uint256"
        }
      ],
      "name": "CrystalOpen",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "crystalId",
          "type": "uint256"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "summonerId",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "assistantId",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint16",
          "name": "generation",
          "type": "uint16"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "createdBlock",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint8",
          "name": "summonerTears",
          "type": "uint8"
        },
        {
          "indexed": False,
          "internalType": "uint8",
          "name": "assistantTears",
          "type": "uint8"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "bonusItem",
          "type": "address"
        }
      ],
      "name": "CrystalSummoned",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "previousOwner",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "newOwner",
          "type": "address"
        }
      ],
      "name": "OwnershipTransferred",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "Paused",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "bytes32",
          "name": "role",
          "type": "bytes32"
        },
        {
          "indexed": True,
          "internalType": "bytes32",
          "name": "previousAdminRole",
          "type": "bytes32"
        },
        {
          "indexed": True,
          "internalType": "bytes32",
          "name": "newAdminRole",
          "type": "bytes32"
        }
      ],
      "name": "RoleAdminChanged",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "bytes32",
          "name": "role",
          "type": "bytes32"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "account",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "sender",
          "type": "address"
        }
      ],
      "name": "RoleGranted",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "bytes32",
          "name": "role",
          "type": "bytes32"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "account",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "sender",
          "type": "address"
        }
      ],
      "name": "RoleRevoked",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "Unpaused",
      "type": "event"
    },
    {
      "inputs": [],
      "name": "DEFAULT_ADMIN_ROLE",
      "outputs": [
        {
          "internalType": "bytes32",
          "name": "",
          "type": "bytes32"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "MODERATOR_ROLE",
      "outputs": [
        {
          "internalType": "bytes32",
          "name": "",
          "type": "bytes32"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "auctionHeroCore",
      "outputs": [
        {
          "internalType": "contract IHeroCore",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "baseCooldown",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "baseSummonFee",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_tokenId",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_bidAmount",
          "type": "uint256"
        }
      ],
      "name": "bid",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "components": [
            {
              "internalType": "uint256",
              "name": "id",
              "type": "uint256"
            },
            {
              "components": [
                {
                  "internalType": "uint256",
                  "name": "summonedTime",
                  "type": "uint256"
                },
                {
                  "internalType": "uint256",
                  "name": "nextSummonTime",
                  "type": "uint256"
                },
                {
                  "internalType": "uint256",
                  "name": "summonerId",
                  "type": "uint256"
                },
                {
                  "internalType": "uint256",
                  "name": "assistantId",
                  "type": "uint256"
                },
                {
                  "internalType": "uint32",
                  "name": "summons",
                  "type": "uint32"
                },
                {
                  "internalType": "uint32",
                  "name": "maxSummons",
                  "type": "uint32"
                }
              ],
              "internalType": "struct IHeroTypes.SummoningInfo",
              "name": "summoningInfo",
              "type": "tuple"
            },
            {
              "components": [
                {
                  "internalType": "uint256",
                  "name": "statGenes",
                  "type": "uint256"
                },
                {
                  "internalType": "uint256",
                  "name": "visualGenes",
                  "type": "uint256"
                },
                {
                  "internalType": "enum IHeroTypes.Rarity",
                  "name": "rarity",
                  "type": "uint8"
                },
                {
                  "internalType": "bool",
                  "name": "shiny",
                  "type": "bool"
                },
                {
                  "internalType": "uint16",
                  "name": "generation",
                  "type": "uint16"
                },
                {
                  "internalType": "uint32",
                  "name": "firstName",
                  "type": "uint32"
                },
                {
                  "internalType": "uint32",
                  "name": "lastName",
                  "type": "uint32"
                },
                {
                  "internalType": "uint8",
                  "name": "shinyStyle",
                  "type": "uint8"
                },
                {
                  "internalType": "uint8",
                  "name": "class",
                  "type": "uint8"
                },
                {
                  "internalType": "uint8",
                  "name": "subClass",
                  "type": "uint8"
                }
              ],
              "internalType": "struct IHeroTypes.HeroInfo",
              "name": "info",
              "type": "tuple"
            },
            {
              "components": [
                {
                  "internalType": "uint256",
                  "name": "staminaFullAt",
                  "type": "uint256"
                },
                {
                  "internalType": "uint256",
                  "name": "hpFullAt",
                  "type": "uint256"
                },
                {
                  "internalType": "uint256",
                  "name": "mpFullAt",
                  "type": "uint256"
                },
                {
                  "internalType": "uint16",
                  "name": "level",
                  "type": "uint16"
                },
                {
                  "internalType": "uint64",
                  "name": "xp",
                  "type": "uint64"
                },
                {
                  "internalType": "address",
                  "name": "currentQuest",
                  "type": "address"
                },
                {
                  "internalType": "uint8",
                  "name": "sp",
                  "type": "uint8"
                },
                {
                  "internalType": "enum IHeroTypes.HeroStatus",
                  "name": "status",
                  "type": "uint8"
                }
              ],
              "internalType": "struct IHeroTypes.HeroState",
              "name": "state",
              "type": "tuple"
            },
            {
              "components": [
                {
                  "internalType": "uint16",
                  "name": "strength",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "intelligence",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "wisdom",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "luck",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "agility",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "vitality",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "endurance",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "dexterity",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "hp",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "mp",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "stamina",
                  "type": "uint16"
                }
              ],
              "internalType": "struct IHeroTypes.HeroStats",
              "name": "stats",
              "type": "tuple"
            },
            {
              "components": [
                {
                  "internalType": "uint16",
                  "name": "strength",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "intelligence",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "wisdom",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "luck",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "agility",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "vitality",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "endurance",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "dexterity",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "hpSm",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "hpRg",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "hpLg",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "mpSm",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "mpRg",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "mpLg",
                  "type": "uint16"
                }
              ],
              "internalType": "struct IHeroTypes.HeroStatGrowth",
              "name": "primaryStatGrowth",
              "type": "tuple"
            },
            {
              "components": [
                {
                  "internalType": "uint16",
                  "name": "strength",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "intelligence",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "wisdom",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "luck",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "agility",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "vitality",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "endurance",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "dexterity",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "hpSm",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "hpRg",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "hpLg",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "mpSm",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "mpRg",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "mpLg",
                  "type": "uint16"
                }
              ],
              "internalType": "struct IHeroTypes.HeroStatGrowth",
              "name": "secondaryStatGrowth",
              "type": "tuple"
            },
            {
              "components": [
                {
                  "internalType": "uint16",
                  "name": "mining",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "gardening",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "foraging",
                  "type": "uint16"
                },
                {
                  "internalType": "uint16",
                  "name": "fishing",
                  "type": "uint16"
                }
              ],
              "internalType": "struct IHeroTypes.HeroProfessions",
              "name": "professions",
              "type": "tuple"
            }
          ],
          "internalType": "struct IHeroTypes.Hero",
          "name": "_hero",
          "type": "tuple"
        }
      ],
      "name": "calculateSummoningCost",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_tokenId",
          "type": "uint256"
        }
      ],
      "name": "cancelAuction",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_tokenId",
          "type": "uint256"
        }
      ],
      "name": "cancelAuctionWhenPaused",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "cooldownPerGen",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_tokenId",
          "type": "uint256"
        },
        {
          "internalType": "uint128",
          "name": "_startingPrice",
          "type": "uint128"
        },
        {
          "internalType": "uint128",
          "name": "_endingPrice",
          "type": "uint128"
        },
        {
          "internalType": "uint64",
          "name": "_duration",
          "type": "uint64"
        },
        {
          "internalType": "address",
          "name": "_winner",
          "type": "address"
        }
      ],
      "name": "createAuction",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "name": "crystals",
      "outputs": [
        {
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "summonerId",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "assistantId",
          "type": "uint256"
        },
        {
          "internalType": "uint16",
          "name": "generation",
          "type": "uint16"
        },
        {
          "internalType": "uint256",
          "name": "createdBlock",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "heroId",
          "type": "uint256"
        },
        {
          "internalType": "uint8",
          "name": "summonerTears",
          "type": "uint8"
        },
        {
          "internalType": "uint8",
          "name": "assistantTears",
          "type": "uint8"
        },
        {
          "internalType": "address",
          "name": "bonusItem",
          "type": "address"
        },
        {
          "internalType": "uint32",
          "name": "maxSummons",
          "type": "uint32"
        },
        {
          "internalType": "uint32",
          "name": "firstName",
          "type": "uint32"
        },
        {
          "internalType": "uint32",
          "name": "lastName",
          "type": "uint32"
        },
        {
          "internalType": "uint8",
          "name": "shinyStyle",
          "type": "uint8"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_rarityRoll",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_rarityMod",
          "type": "uint256"
        }
      ],
      "name": "determineRarity",
      "outputs": [
        {
          "internalType": "enum IHeroTypes.Rarity",
          "name": "",
          "type": "uint8"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "enabled",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "randomNumber",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "digits",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "offset",
          "type": "uint256"
        }
      ],
      "name": "extractNumber",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "result",
          "type": "uint256"
        }
      ],
      "stateMutability": "pure",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_tokenId",
          "type": "uint256"
        }
      ],
      "name": "getAuction",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "auctionId",
          "type": "uint256"
        },
        {
          "internalType": "address",
          "name": "seller",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "startingPrice",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "endingPrice",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "duration",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "startedAt",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_crystalId",
          "type": "uint256"
        }
      ],
      "name": "getCrystal",
      "outputs": [
        {
          "components": [
            {
              "internalType": "address",
              "name": "owner",
              "type": "address"
            },
            {
              "internalType": "uint256",
              "name": "summonerId",
              "type": "uint256"
            },
            {
              "internalType": "uint256",
              "name": "assistantId",
              "type": "uint256"
            },
            {
              "internalType": "uint16",
              "name": "generation",
              "type": "uint16"
            },
            {
              "internalType": "uint256",
              "name": "createdBlock",
              "type": "uint256"
            },
            {
              "internalType": "uint256",
              "name": "heroId",
              "type": "uint256"
            },
            {
              "internalType": "uint8",
              "name": "summonerTears",
              "type": "uint8"
            },
            {
              "internalType": "uint8",
              "name": "assistantTears",
              "type": "uint8"
            },
            {
              "internalType": "address",
              "name": "bonusItem",
              "type": "address"
            },
            {
              "internalType": "uint32",
              "name": "maxSummons",
              "type": "uint32"
            },
            {
              "internalType": "uint32",
              "name": "firstName",
              "type": "uint32"
            },
            {
              "internalType": "uint32",
              "name": "lastName",
              "type": "uint32"
            },
            {
              "internalType": "uint8",
              "name": "shinyStyle",
              "type": "uint8"
            }
          ],
          "internalType": "struct ICrystalTypes.HeroCrystal",
          "name": "",
          "type": "tuple"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_tokenId",
          "type": "uint256"
        }
      ],
      "name": "getCurrentPrice",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "role",
          "type": "bytes32"
        }
      ],
      "name": "getRoleAdmin",
      "outputs": [
        {
          "internalType": "bytes32",
          "name": "",
          "type": "bytes32"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_address",
          "type": "address"
        }
      ],
      "name": "getUserAuctions",
      "outputs": [
        {
          "internalType": "uint256[]",
          "name": "",
          "type": "uint256[]"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_address",
          "type": "address"
        }
      ],
      "name": "getUserCrystals",
      "outputs": [
        {
          "internalType": "uint256[]",
          "name": "",
          "type": "uint256[]"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "role",
          "type": "bytes32"
        },
        {
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "grantRole",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "role",
          "type": "bytes32"
        },
        {
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "hasRole",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "increasePerGen",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "increasePerSummon",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_heroCoreAddress",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "_geneScienceAddress",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "_jewelTokenAddress",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "_gaiaTearsAddress",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "_statScienceAddress",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "_cut",
          "type": "uint256"
        }
      ],
      "name": "initialize",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_tokenId",
          "type": "uint256"
        }
      ],
      "name": "isOnAuction",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "jewelToken",
      "outputs": [
        {
          "internalType": "contract IJewelToken",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "maxPrice",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "minPrice",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "newSummonCooldown",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_crystalId",
          "type": "uint256"
        }
      ],
      "name": "open",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "owner",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "ownerCut",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "paused",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_crystalId",
          "type": "uint256"
        }
      ],
      "name": "rechargeCrystal",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "renounceOwnership",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "role",
          "type": "bytes32"
        },
        {
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "renounceRole",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "role",
          "type": "bytes32"
        },
        {
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "revokeRole",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address[]",
          "name": "_feeAddresses",
          "type": "address[]"
        },
        {
          "internalType": "uint256[]",
          "name": "_feePercents",
          "type": "uint256[]"
        }
      ],
      "name": "setFees",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_geneScienceAddress",
          "type": "address"
        }
      ],
      "name": "setGeneScienceAddress",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_min",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_max",
          "type": "uint256"
        }
      ],
      "name": "setLimits",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_statScienceAddress",
          "type": "address"
        }
      ],
      "name": "setStatScienceAddress",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_newSummonCooldown",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_baseCooldown",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_cooldownPerGen",
          "type": "uint256"
        }
      ],
      "name": "setSummonCooldowns",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_baseSummonFee",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_increasePerSummon",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_increasePerGen",
          "type": "uint256"
        }
      ],
      "name": "setSummonFees",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "statScience",
      "outputs": [
        {
          "internalType": "contract IStatScience",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_summonerId",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_assistantId",
          "type": "uint256"
        },
        {
          "internalType": "uint16",
          "name": "_summonerTears",
          "type": "uint16"
        },
        {
          "internalType": "uint16",
          "name": "_assistantTears",
          "type": "uint16"
        },
        {
          "internalType": "address",
          "name": "_bonusItem",
          "type": "address"
        }
      ],
      "name": "summonCrystal",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes4",
          "name": "interfaceId",
          "type": "bytes4"
        }
      ],
      "name": "supportsInterface",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "toggleEnabled",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "newOwner",
          "type": "address"
        }
      ],
      "name": "transferOwnership",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "name": "userAuctions",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "name": "userCrystals",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "blockNumber",
          "type": "uint256"
        }
      ],
      "name": "vrf",
      "outputs": [
        {
          "internalType": "bytes32",
          "name": "result",
          "type": "bytes32"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    }
  ]

w3 = Web3(Web3.HTTPProvider(settings.RPC_ADDRESS))

CONTRACT = w3.eth.contract(Web3.toChecksumAddress(CONTRACT_ADDRESS), abi=ABI)
