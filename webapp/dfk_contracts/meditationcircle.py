from django.conf import settings
from web3 import Web3

CONTRACT_ADDRESS = '0x0594D86b2923076a2316EaEA4E1Ca286dAA142C1'

ABI = [
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "internalType": "address",
          "name": "atunementItemAddress",
          "type": "address"
        }
      ],
      "name": "AttunementCrystalAdded",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "player",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "uint256",
          "name": "heroId",
          "type": "uint256"
        },
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
          "indexed": False,
          "internalType": "struct IHeroTypes.Hero",
          "name": "hero",
          "type": "tuple"
        },
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
          "indexed": False,
          "internalType": "struct IHeroTypes.Hero",
          "name": "oldHero",
          "type": "tuple"
        }
      ],
      "name": "LevelUp",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "player",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "uint256",
          "name": "heroId",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "meditationId",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint8",
          "name": "primaryStat",
          "type": "uint8"
        },
        {
          "indexed": False,
          "internalType": "uint8",
          "name": "secondaryStat",
          "type": "uint8"
        },
        {
          "indexed": False,
          "internalType": "uint8",
          "name": "tertiaryStat",
          "type": "uint8"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "attunementCrystal",
          "type": "address"
        }
      ],
      "name": "MeditationBegun",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "player",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "uint256",
          "name": "heroId",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "meditationId",
          "type": "uint256"
        }
      ],
      "name": "MeditationCompleted",
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
          "indexed": True,
          "internalType": "address",
          "name": "player",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "uint256",
          "name": "heroId",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "stat",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint8",
          "name": "increase",
          "type": "uint8"
        },
        {
          "indexed": False,
          "internalType": "enum MeditationCircle.UpdateType",
          "name": "updateType",
          "type": "uint8"
        }
      ],
      "name": "StatUp",
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
      "inputs": [
        {
          "internalType": "uint16",
          "name": "_level",
          "type": "uint16"
        }
      ],
      "name": "_getRequiredRunes",
      "outputs": [
        {
          "internalType": "uint16[10]",
          "name": "",
          "type": "uint16[10]"
        }
      ],
      "stateMutability": "pure",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "name": "activeAttunementCrystals",
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
          "internalType": "address",
          "name": "_address",
          "type": "address"
        }
      ],
      "name": "addAttunementCrystal",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_heroId",
          "type": "uint256"
        }
      ],
      "name": "completeMeditation",
      "outputs": [],
      "stateMutability": "nonpayable",
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
          "internalType": "address",
          "name": "_address",
          "type": "address"
        }
      ],
      "name": "getActiveMeditations",
      "outputs": [
        {
          "components": [
            {
              "internalType": "uint256",
              "name": "id",
              "type": "uint256"
            },
            {
              "internalType": "address",
              "name": "player",
              "type": "address"
            },
            {
              "internalType": "uint256",
              "name": "heroId",
              "type": "uint256"
            },
            {
              "internalType": "uint8",
              "name": "primaryStat",
              "type": "uint8"
            },
            {
              "internalType": "uint8",
              "name": "secondaryStat",
              "type": "uint8"
            },
            {
              "internalType": "uint8",
              "name": "tertiaryStat",
              "type": "uint8"
            },
            {
              "internalType": "address",
              "name": "attunementCrystal",
              "type": "address"
            },
            {
              "internalType": "uint256",
              "name": "startBlock",
              "type": "uint256"
            },
            {
              "internalType": "uint8",
              "name": "status",
              "type": "uint8"
            }
          ],
          "internalType": "struct MeditationCircle.Meditation[]",
          "name": "",
          "type": "tuple[]"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_heroId",
          "type": "uint256"
        }
      ],
      "name": "getHeroMeditation",
      "outputs": [
        {
          "components": [
            {
              "internalType": "uint256",
              "name": "id",
              "type": "uint256"
            },
            {
              "internalType": "address",
              "name": "player",
              "type": "address"
            },
            {
              "internalType": "uint256",
              "name": "heroId",
              "type": "uint256"
            },
            {
              "internalType": "uint8",
              "name": "primaryStat",
              "type": "uint8"
            },
            {
              "internalType": "uint8",
              "name": "secondaryStat",
              "type": "uint8"
            },
            {
              "internalType": "uint8",
              "name": "tertiaryStat",
              "type": "uint8"
            },
            {
              "internalType": "address",
              "name": "attunementCrystal",
              "type": "address"
            },
            {
              "internalType": "uint256",
              "name": "startBlock",
              "type": "uint256"
            },
            {
              "internalType": "uint8",
              "name": "status",
              "type": "uint8"
            }
          ],
          "internalType": "struct MeditationCircle.Meditation",
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
          "name": "_id",
          "type": "uint256"
        }
      ],
      "name": "getMeditation",
      "outputs": [
        {
          "components": [
            {
              "internalType": "uint256",
              "name": "id",
              "type": "uint256"
            },
            {
              "internalType": "address",
              "name": "player",
              "type": "address"
            },
            {
              "internalType": "uint256",
              "name": "heroId",
              "type": "uint256"
            },
            {
              "internalType": "uint8",
              "name": "primaryStat",
              "type": "uint8"
            },
            {
              "internalType": "uint8",
              "name": "secondaryStat",
              "type": "uint8"
            },
            {
              "internalType": "uint8",
              "name": "tertiaryStat",
              "type": "uint8"
            },
            {
              "internalType": "address",
              "name": "attunementCrystal",
              "type": "address"
            },
            {
              "internalType": "uint256",
              "name": "startBlock",
              "type": "uint256"
            },
            {
              "internalType": "uint8",
              "name": "status",
              "type": "uint8"
            }
          ],
          "internalType": "struct MeditationCircle.Meditation",
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
      "inputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "name": "heroToMeditation",
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
          "name": "_statScienceAddress",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "_jewelTokenAddress",
          "type": "address"
        }
      ],
      "name": "initialize",
      "outputs": [],
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
      "name": "pause",
      "outputs": [],
      "stateMutability": "nonpayable",
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
      "name": "profileActiveMeditations",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "id",
          "type": "uint256"
        },
        {
          "internalType": "address",
          "name": "player",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "heroId",
          "type": "uint256"
        },
        {
          "internalType": "uint8",
          "name": "primaryStat",
          "type": "uint8"
        },
        {
          "internalType": "uint8",
          "name": "secondaryStat",
          "type": "uint8"
        },
        {
          "internalType": "uint8",
          "name": "tertiaryStat",
          "type": "uint8"
        },
        {
          "internalType": "address",
          "name": "attunementCrystal",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "startBlock",
          "type": "uint256"
        },
        {
          "internalType": "uint8",
          "name": "status",
          "type": "uint8"
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
          "internalType": "uint8",
          "name": "_index",
          "type": "uint8"
        },
        {
          "internalType": "address",
          "name": "_address",
          "type": "address"
        }
      ],
      "name": "setRune",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_heroId",
          "type": "uint256"
        },
        {
          "internalType": "uint8",
          "name": "_primaryStat",
          "type": "uint8"
        },
        {
          "internalType": "uint8",
          "name": "_secondaryStat",
          "type": "uint8"
        },
        {
          "internalType": "uint8",
          "name": "_tertiaryStat",
          "type": "uint8"
        },
        {
          "internalType": "address",
          "name": "_attunementCrystal",
          "type": "address"
        }
      ],
      "name": "startMeditation",
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
      "name": "unpause",
      "outputs": [],
      "stateMutability": "nonpayable",
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
