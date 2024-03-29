from django.conf import settings
from web3 import Web3

CONTRACT_ADDRESS = "0xDB30643c71aC9e2122cA0341ED77d09D5f99F924"

ABI = [
    {
        "inputs": [
            {
                "internalType": "contract JewelToken",
                "name": "_govToken",
                "type": "address"
            },
            {
                "name": "_devaddr",
                "internalType": "address",
                "type": "address"
            },
            {
                "type": "address",
                "internalType": "address",
                "name": "_liquidityaddr"
            },
            {
                "type": "address",
                "name": "_comfundaddr",
                "internalType": "address"
            },
            {
                "name": "_founderaddr",
                "type": "address",
                "internalType": "address"
            },
            {
                "internalType": "uint256",
                "name": "_rewardPerBlock",
                "type": "uint256"
            },
            {
                "name": "_startBlock",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "type": "uint256",
                "internalType": "uint256",
                "name": "_halvingAfterBlock"
            },
            {
                "internalType": "uint256",
                "type": "uint256",
                "name": "_userDepFee"
            },
            {
                "internalType": "uint256",
                "name": "_devDepFee",
                "type": "uint256"
            },
            {
                "type": "uint256[]",
                "name": "_rewardMultiplier",
                "internalType": "uint256[]"
            },
            {
                "type": "uint256[]",
                "internalType": "uint256[]",
                "name": "_blockDeltaStartStage"
            },
            {
                "name": "_blockDeltaEndStage",
                "type": "uint256[]",
                "internalType": "uint256[]"
            },
            {
                "type": "uint256[]",
                "name": "_userFeeStage",
                "internalType": "uint256[]"
            },
            {
                "internalType": "uint256[]",
                "name": "_devFeeStage",
                "type": "uint256[]"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "inputs": [
            {
                "type": "address",
                "internalType": "address",
                "indexed": True,
                "name": "user"
            },
            {
                "indexed": True,
                "internalType": "uint256",
                "type": "uint256",
                "name": "pid"
            },
            {
                "name": "amount",
                "type": "uint256",
                "internalType": "uint256",
                "indexed": False
            }
        ],
        "anonymous": False,
        "name": "Deposit",
        "type": "event"
    },
    {
        "name": "EmergencyWithdraw",
        "inputs": [
            {
                "internalType": "address",
                "type": "address",
                "indexed": True,
                "name": "user"
            },
            {
                "indexed": True,
                "name": "pid",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "type": "uint256",
                "internalType": "uint256",
                "indexed": False,
                "name": "amount"
            }
        ],
        "type": "event",
        "anonymous": False
    },
    {
        "inputs": [
            {
                "indexed": True,
                "name": "previousOwner",
                "type": "address",
                "internalType": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "type": "address",
                "name": "newOwner"
            }
        ],
        "anonymous": False,
        "name": "OwnershipTransferred",
        "type": "event"
    },
    {
        "type": "event",
        "name": "SendGovernanceTokenReward",
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "type": "address",
                "internalType": "address",
                "name": "user"
            },
            {
                "indexed": True,
                "name": "pid",
                "internalType": "uint256",
                "type": "uint256"
            },
            {
                "name": "amount",
                "type": "uint256",
                "indexed": False,
                "internalType": "uint256"
            },
            {
                "type": "uint256",
                "internalType": "uint256",
                "name": "lockAmount",
                "indexed": False
            }
        ]
    },
    {
        "type": "event",
        "anonymous": False,
        "name": "Withdraw",
        "inputs": [
            {
                "name": "user",
                "type": "address",
                "indexed": True,
                "internalType": "address"
            },
            {
                "type": "uint256",
                "internalType": "uint256",
                "indexed": True,
                "name": "pid"
            },
            {
                "name": "amount",
                "internalType": "uint256",
                "indexed": False,
                "type": "uint256"
            }
        ]
    },
    {
        "inputs": [],
        "type": "function",
        "outputs": [
            {
                "name": "",
                "internalType": "uint256",
                "type": "uint256"
            }
        ],
        "name": "FINISH_BONUS_AT_BLOCK",
        "stateMutability": "view"
    },
    {
        "type": "function",
        "name": "HALVING_AT_BLOCK",
        "stateMutability": "view",
        "outputs": [
            {
                "name": "",
                "internalType": "uint256",
                "type": "uint256"
            }
        ],
        "inputs": [
            {
                "type": "uint256",
                "name": "",
                "internalType": "uint256"
            }
        ]
    },
    {
        "type": "function",
        "name": "PERCENT_FOR_COM",
        "stateMutability": "view",
        "outputs": [
            {
                "name": "",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "inputs": []
    },
    {
        "stateMutability": "view",
        "outputs": [
            {
                "internalType": "uint256",
                "type": "uint256",
                "name": ""
            }
        ],
        "name": "PERCENT_FOR_DEV",
        "type": "function",
        "inputs": []
    },
    {
        "name": "PERCENT_FOR_FOUNDERS",
        "stateMutability": "view",
        "outputs": [
            {
                "name": "",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "type": "function",
        "inputs": []
    },
    {
        "stateMutability": "view",
        "name": "PERCENT_FOR_LP",
        "inputs": [],
        "outputs": [
            {
                "internalType": "uint256",
                "type": "uint256",
                "name": ""
            }
        ],
        "type": "function"
    },
    {
        "name": "PERCENT_LOCK_BONUS_REWARD",
        "inputs": [
            {
                "name": "",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
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
        "stateMutability": "view",
        "name": "REWARD_MULTIPLIER",
        "inputs": [
            {
                "name": "",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "type": "function",
        "outputs": [
            {
                "name": "",
                "internalType": "uint256",
                "type": "uint256"
            }
        ]
    },
    {
        "name": "REWARD_PER_BLOCK",
        "outputs": [
            {
                "type": "uint256",
                "name": "",
                "internalType": "uint256"
            }
        ],
        "type": "function",
        "stateMutability": "view",
        "inputs": []
    },
    {
        "outputs": [
            {
                "type": "uint256",
                "name": "",
                "internalType": "uint256"
            }
        ],
        "stateMutability": "view",
        "inputs": [],
        "name": "START_BLOCK",
        "type": "function"
    },
    {
        "inputs": [
            {
                "name": "_toAdd",
                "internalType": "address",
                "type": "address"
            }
        ],
        "name": "addAuthorized",
        "type": "function",
        "outputs": [],
        "stateMutability": "nonpayable"
    },
    {
        "outputs": [
            {
                "internalType": "bool",
                "type": "bool",
                "name": ""
            }
        ],
        "stateMutability": "view",
        "type": "function",
        "name": "authorized",
        "inputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ]
    },
    {
        "type": "function",
        "stateMutability": "view",
        "inputs": [
            {
                "name": "",
                "internalType": "uint256",
                "type": "uint256"
            }
        ],
        "outputs": [
            {
                "name": "",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "name": "blockDeltaEndStage"
    },
    {
        "stateMutability": "view",
        "inputs": [
            {
                "type": "uint256",
                "name": "",
                "internalType": "uint256"
            }
        ],
        "name": "blockDeltaStartStage",
        "type": "function",
        "outputs": [
            {
                "type": "uint256",
                "internalType": "uint256",
                "name": ""
            }
        ]
    },
    {
        "stateMutability": "view",
        "type": "function",
        "inputs": [],
        "name": "comfundaddr",
        "outputs": [
            {
                "name": "",
                "type": "address",
                "internalType": "address"
            }
        ]
    },
    {
        "type": "function",
        "inputs": [],
        "name": "devDepFee",
        "stateMutability": "view",
        "outputs": [
            {
                "type": "uint256",
                "internalType": "uint256",
                "name": ""
            }
        ]
    },
    {
        "stateMutability": "view",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "name": "devFeeStage",
        "inputs": [
            {
                "name": "",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "type": "function"
    },
    {
        "outputs": [
            {
                "name": "",
                "type": "address",
                "internalType": "address"
            }
        ],
        "stateMutability": "view",
        "name": "devaddr",
        "type": "function",
        "inputs": []
    },
    {
        "inputs": [],
        "name": "founderaddr",
        "stateMutability": "view",
        "outputs": [
            {
                "type": "address",
                "name": "",
                "internalType": "address"
            }
        ],
        "type": "function"
    },
    {
        "stateMutability": "view",
        "inputs": [],
        "name": "govToken",
        "outputs": [
            {
                "type": "address",
                "name": "",
                "internalType": "contract JewelToken"
            }
        ],
        "type": "function"
    },
    {
        "name": "liquidityaddr",
        "stateMutability": "view",
        "inputs": [],
        "type": "function",
        "outputs": [
            {
                "type": "address",
                "name": "",
                "internalType": "address"
            }
        ]
    },
    {
        "type": "function",
        "outputs": [
            {
                "type": "address",
                "internalType": "address",
                "name": ""
            }
        ],
        "name": "owner",
        "inputs": [],
        "stateMutability": "view"
    },
    {
        "name": "poolExistence",
        "outputs": [
            {
                "name": "",
                "type": "bool",
                "internalType": "bool"
            }
        ],
        "type": "function",
        "stateMutability": "view",
        "inputs": [
            {
                "type": "address",
                "name": "",
                "internalType": "contract IERC20"
            }
        ]
    },
    {
        "stateMutability": "view",
        "name": "poolId1",
        "type": "function",
        "inputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "outputs": [
            {
                "name": "",
                "internalType": "uint256",
                "type": "uint256"
            }
        ]
    },
    {
        "inputs": [
            {
                "name": "",
                "internalType": "uint256",
                "type": "uint256"
            }
        ],
        "outputs": [
            {
                "internalType": "contract IERC20",
                "name": "lpToken",
                "type": "address"
            },
            {
                "name": "allocPoint",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "name": "lastRewardBlock",
                "internalType": "uint256",
                "type": "uint256"
            },
            {
                "name": "accGovTokenPerShare",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "type": "function",
        "name": "poolInfo",
        "stateMutability": "view"
    },
    {
        "inputs": [
            {
                "name": "_toRemove",
                "type": "address",
                "internalType": "address"
            }
        ],
        "outputs": [],
        "name": "removeAuthorized",
        "type": "function",
        "stateMutability": "nonpayable"
    },
    {
        "stateMutability": "nonpayable",
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "type": "function"
    },
    {
        "outputs": [
            {
                "internalType": "uint256",
                "type": "uint256",
                "name": ""
            }
        ],
        "type": "function",
        "name": "totalAllocPoint",
        "inputs": [],
        "stateMutability": "view"
    },
    {
        "outputs": [],
        "type": "function",
        "stateMutability": "nonpayable",
        "inputs": [
            {
                "internalType": "address",
                "type": "address",
                "name": "newOwner"
            }
        ],
        "name": "transferOwnership"
    },
    {
        "stateMutability": "view",
        "inputs": [],
        "outputs": [
            {
                "name": "",
                "internalType": "address",
                "type": "address"
            }
        ],
        "type": "function",
        "name": "usdOracle"
    },
    {
        "stateMutability": "view",
        "name": "userDepFee",
        "type": "function",
        "inputs": [],
        "outputs": [
            {
                "internalType": "uint256",
                "type": "uint256",
                "name": ""
            }
        ]
    },
    {
        "inputs": [
            {
                "name": "",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "outputs": [
            {
                "name": "",
                "internalType": "uint256",
                "type": "uint256"
            }
        ],
        "name": "userFeeStage",
        "type": "function",
        "stateMutability": "view"
    },
    {
        "name": "userGlobalInfo",
        "outputs": [
            {
                "name": "globalAmount",
                "internalType": "uint256",
                "type": "uint256"
            },
            {
                "type": "uint256",
                "internalType": "uint256",
                "name": "totalReferals"
            },
            {
                "name": "globalRefAmount",
                "internalType": "uint256",
                "type": "uint256"
            }
        ],
        "type": "function",
        "stateMutability": "view",
        "inputs": [
            {
                "type": "address",
                "internalType": "address",
                "name": ""
            }
        ]
    },
    {
        "outputs": [
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            },
            {
                "type": "uint256",
                "name": "rewardDebt",
                "internalType": "uint256"
            },
            {
                "name": "rewardDebtAtBlock",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "type": "uint256",
                "name": "lastWithdrawBlock",
                "internalType": "uint256"
            },
            {
                "type": "uint256",
                "internalType": "uint256",
                "name": "firstDepositBlock"
            },
            {
                "internalType": "uint256",
                "type": "uint256",
                "name": "blockdelta"
            },
            {
                "name": "lastDepositBlock",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "type": "function",
        "stateMutability": "view",
        "inputs": [
            {
                "internalType": "uint256",
                "type": "uint256",
                "name": ""
            },
            {
                "type": "address",
                "name": "",
                "internalType": "address"
            }
        ],
        "name": "userInfo"
    },
    {
        "type": "function",
        "inputs": [],
        "stateMutability": "view",
        "name": "poolLength",
        "outputs": [
            {
                "type": "uint256",
                "name": "",
                "internalType": "uint256"
            }
        ]
    },
    {
        "name": "add",
        "stateMutability": "nonpayable",
        "inputs": [
            {
                "type": "uint256",
                "name": "_allocPoint",
                "internalType": "uint256"
            },
            {
                "type": "address",
                "internalType": "contract IERC20",
                "name": "_lpToken"
            },
            {
                "internalType": "bool",
                "type": "bool",
                "name": "_withUpdate"
            }
        ],
        "type": "function",
        "outputs": []
    },
    {
        "inputs": [
            {
                "name": "_pid",
                "internalType": "uint256",
                "type": "uint256"
            },
            {
                "type": "uint256",
                "internalType": "uint256",
                "name": "_allocPoint"
            },
            {
                "internalType": "bool",
                "name": "_withUpdate",
                "type": "bool"
            }
        ],
        "name": "set",
        "type": "function",
        "outputs": [],
        "stateMutability": "nonpayable"
    },
    {
        "name": "massUpdatePools",
        "outputs": [],
        "inputs": [],
        "type": "function",
        "stateMutability": "nonpayable"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "type": "uint256",
                "name": "_pid"
            }
        ],
        "outputs": [],
        "type": "function",
        "stateMutability": "nonpayable",
        "name": "updatePool"
    },
    {
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "name": "getMultiplier",
        "stateMutability": "view",
        "type": "function",
        "inputs": [
            {
                "type": "uint256",
                "name": "_from",
                "internalType": "uint256"
            },
            {
                "type": "uint256",
                "internalType": "uint256",
                "name": "_to"
            }
        ]
    },
    {
        "type": "function",
        "outputs": [
            {
                "internalType": "uint256",
                "type": "uint256",
                "name": ""
            }
        ],
        "name": "getLockPercentage",
        "stateMutability": "view",
        "inputs": [
            {
                "name": "_from",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "_to",
                "type": "uint256"
            }
        ]
    },
    {
        "type": "function",
        "name": "getPoolReward",
        "stateMutability": "view",
        "inputs": [
            {
                "name": "_from",
                "internalType": "uint256",
                "type": "uint256"
            },
            {
                "name": "_to",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "_allocPoint",
                "type": "uint256"
            }
        ],
        "outputs": [
            {
                "type": "uint256",
                "name": "forDev",
                "internalType": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "forFarmer",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "type": "uint256",
                "name": "forLP"
            },
            {
                "internalType": "uint256",
                "name": "forCom",
                "type": "uint256"
            },
            {
                "type": "uint256",
                "name": "forFounders",
                "internalType": "uint256"
            }
        ]
    },
    {
        "stateMutability": "view",
        "name": "pendingReward",
        "type": "function",
        "outputs": [
            {
                "name": "",
                "internalType": "uint256",
                "type": "uint256"
            }
        ],
        "inputs": [
            {
                "name": "_pid",
                "internalType": "uint256",
                "type": "uint256"
            },
            {
                "type": "address",
                "internalType": "address",
                "name": "_user"
            }
        ]
    },
    {
        "inputs": [
            {
                "name": "_pids",
                "internalType": "uint256[]",
                "type": "uint256[]"
            }
        ],
        "outputs": [],
        "name": "claimRewards",
        "type": "function",
        "stateMutability": "nonpayable"
    },
    {
        "inputs": [
            {
                "name": "_pid",
                "internalType": "uint256",
                "type": "uint256"
            }
        ],
        "name": "claimReward",
        "type": "function",
        "stateMutability": "nonpayable",
        "outputs": []
    },
    {
        "name": "getGlobalAmount",
        "type": "function",
        "stateMutability": "view",
        "inputs": [
            {
                "type": "address",
                "name": "_user",
                "internalType": "address"
            }
        ],
        "outputs": [
            {
                "name": "",
                "type": "uint256",
                "internalType": "uint256"
            }
        ]
    },
    {
        "type": "function",
        "outputs": [
            {
                "name": "",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "name": "getGlobalRefAmount",
        "stateMutability": "view",
        "inputs": [
            {
                "name": "_user",
                "internalType": "address",
                "type": "address"
            }
        ]
    },
    {
        "stateMutability": "view",
        "inputs": [
            {
                "type": "address",
                "internalType": "address",
                "name": "_user"
            }
        ],
        "name": "getTotalRefs",
        "type": "function",
        "outputs": [
            {
                "internalType": "uint256",
                "type": "uint256",
                "name": ""
            }
        ]
    },
    {
        "type": "function",
        "inputs": [
            {
                "internalType": "address",
                "type": "address",
                "name": "_user"
            },
            {
                "internalType": "address",
                "name": "_user2",
                "type": "address"
            }
        ],
        "name": "getRefValueOf",
        "stateMutability": "view",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ]
    },
    {
        "stateMutability": "nonpayable",
        "outputs": [],
        "type": "function",
        "inputs": [
            {
                "type": "uint256",
                "name": "_pid",
                "internalType": "uint256"
            },
            {
                "internalType": "uint256",
                "type": "uint256",
                "name": "_amount"
            },
            {
                "name": "_ref",
                "type": "address",
                "internalType": "address"
            }
        ],
        "name": "deposit"
    },
    {
        "name": "withdraw",
        "outputs": [],
        "inputs": [
            {
                "type": "uint256",
                "name": "_pid",
                "internalType": "uint256"
            },
            {
                "type": "uint256",
                "name": "_amount",
                "internalType": "uint256"
            },
            {
                "type": "address",
                "name": "_ref",
                "internalType": "address"
            }
        ],
        "type": "function",
        "stateMutability": "nonpayable"
    },
    {
        "type": "function",
        "name": "emergencyWithdraw",
        "outputs": [],
        "stateMutability": "nonpayable",
        "inputs": [
            {
                "name": "_pid",
                "internalType": "uint256",
                "type": "uint256"
            }
        ]
    },
    {
        "type": "function",
        "outputs": [],
        "inputs": [
            {
                "internalType": "address",
                "name": "_devaddr",
                "type": "address"
            }
        ],
        "name": "dev",
        "stateMutability": "nonpayable"
    },
    {
        "stateMutability": "nonpayable",
        "inputs": [
            {
                "name": "_newFinish",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "outputs": [],
        "name": "bonusFinishUpdate",
        "type": "function"
    },
    {
        "name": "halvingUpdate",
        "type": "function",
        "inputs": [
            {
                "internalType": "uint256[]",
                "type": "uint256[]",
                "name": "_newHalving"
            }
        ],
        "outputs": [],
        "stateMutability": "nonpayable"
    },
    {
        "name": "lpUpdate",
        "type": "function",
        "outputs": [],
        "inputs": [
            {
                "type": "address",
                "internalType": "address",
                "name": "_newLP"
            }
        ],
        "stateMutability": "nonpayable"
    },
    {
        "type": "function",
        "stateMutability": "nonpayable",
        "inputs": [
            {
                "name": "_newCom",
                "type": "address",
                "internalType": "address"
            }
        ],
        "name": "comUpdate",
        "outputs": []
    },
    {
        "stateMutability": "nonpayable",
        "outputs": [],
        "type": "function",
        "name": "founderUpdate",
        "inputs": [
            {
                "type": "address",
                "internalType": "address",
                "name": "_newFounder"
            }
        ]
    },
    {
        "inputs": [
            {
                "name": "_newReward",
                "internalType": "uint256",
                "type": "uint256"
            }
        ],
        "outputs": [],
        "type": "function",
        "name": "rewardUpdate",
        "stateMutability": "nonpayable"
    },
    {
        "outputs": [],
        "type": "function",
        "stateMutability": "nonpayable",
        "name": "rewardMulUpdate",
        "inputs": [
            {
                "name": "_newMulReward",
                "type": "uint256[]",
                "internalType": "uint256[]"
            }
        ]
    },
    {
        "inputs": [
            {
                "type": "uint256[]",
                "name": "_newlock",
                "internalType": "uint256[]"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function",
        "outputs": [],
        "name": "lockUpdate"
    },
    {
        "inputs": [
            {
                "name": "_newdevlock",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "name": "lockdevUpdate",
        "outputs": [],
        "type": "function",
        "stateMutability": "nonpayable"
    },
    {
        "type": "function",
        "name": "locklpUpdate",
        "stateMutability": "nonpayable",
        "inputs": [
            {
                "name": "_newlplock",
                "internalType": "uint256",
                "type": "uint256"
            }
        ],
        "outputs": []
    },
    {
        "type": "function",
        "stateMutability": "nonpayable",
        "outputs": [],
        "inputs": [
            {
                "type": "uint256",
                "name": "_newcomlock",
                "internalType": "uint256"
            }
        ],
        "name": "lockcomUpdate"
    },
    {
        "name": "lockfounderUpdate",
        "type": "function",
        "inputs": [
            {
                "name": "_newfounderlock",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "outputs": [],
        "stateMutability": "nonpayable"
    },
    {
        "type": "function",
        "outputs": [],
        "name": "starblockUpdate",
        "inputs": [
            {
                "name": "_newstarblock",
                "internalType": "uint256",
                "type": "uint256"
            }
        ],
        "stateMutability": "nonpayable"
    },
    {
        "name": "getNewRewardPerBlock",
        "type": "function",
        "stateMutability": "view",
        "outputs": [
            {
                "name": "",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "inputs": [
            {
                "internalType": "uint256",
                "name": "pid1",
                "type": "uint256"
            }
        ]
    },
    {
        "name": "userDelta",
        "inputs": [
            {
                "internalType": "uint256",
                "type": "uint256",
                "name": "_pid"
            }
        ],
        "stateMutability": "view",
        "type": "function",
        "outputs": [
            {
                "type": "uint256",
                "name": "",
                "internalType": "uint256"
            }
        ]
    },
    {
        "name": "reviseWithdraw",
        "outputs": [],
        "type": "function",
        "stateMutability": "nonpayable",
        "inputs": [
            {
                "name": "_pid",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "name": "_user",
                "internalType": "address",
                "type": "address"
            },
            {
                "type": "uint256",
                "name": "_block",
                "internalType": "uint256"
            }
        ]
    },
    {
        "stateMutability": "nonpayable",
        "outputs": [],
        "name": "reviseDeposit",
        "type": "function",
        "inputs": [
            {
                "type": "uint256",
                "internalType": "uint256",
                "name": "_pid"
            },
            {
                "type": "address",
                "name": "_user",
                "internalType": "address"
            },
            {
                "type": "uint256",
                "internalType": "uint256",
                "name": "_block"
            }
        ]
    },
    {
        "name": "setStageStarts",
        "outputs": [],
        "type": "function",
        "stateMutability": "nonpayable",
        "inputs": [
            {
                "name": "_blockStarts",
                "type": "uint256[]",
                "internalType": "uint256[]"
            }
        ]
    },
    {
        "type": "function",
        "name": "setStageEnds",
        "outputs": [],
        "inputs": [
            {
                "internalType": "uint256[]",
                "type": "uint256[]",
                "name": "_blockEnds"
            }
        ],
        "stateMutability": "nonpayable"
    },
    {
        "stateMutability": "nonpayable",
        "inputs": [
            {
                "type": "uint256[]",
                "name": "_userFees",
                "internalType": "uint256[]"
            }
        ],
        "name": "setUserFeeStage",
        "type": "function",
        "outputs": []
    },
    {
        "type": "function",
        "name": "setDevFeeStage",
        "stateMutability": "nonpayable",
        "inputs": [
            {
                "type": "uint256[]",
                "name": "_devFees",
                "internalType": "uint256[]"
            }
        ],
        "outputs": []
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_devDepFees",
                "type": "uint256"
            }
        ],
        "type": "function",
        "stateMutability": "nonpayable",
        "outputs": [],
        "name": "setDevDepFee"
    },
    {
        "stateMutability": "nonpayable",
        "name": "setUserDepFee",
        "inputs": [
            {
                "name": "_usrDepFees",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "outputs": [],
        "type": "function"
    },
    {
        "type": "function",
        "stateMutability": "nonpayable",
        "name": "reclaimTokenOwnership",
        "outputs": [],
        "inputs": [
            {
                "type": "address",
                "internalType": "address",
                "name": "_newOwner"
            }
        ]
    }
]

w3 = Web3(Web3.HTTPProvider(settings.RPC_ADDRESS))

CONTRACT = w3.eth.contract(Web3.toChecksumAddress(CONTRACT_ADDRESS), abi=ABI)
