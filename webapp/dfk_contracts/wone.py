from django.conf import settings
from web3 import Web3

# also known as jeweltoken

CONTRACT_ADDRESS = "0xcF664087a5bB0237a0BAd6742852ec6c8d69A27a"

ABI = [
    {
        "anonymous": False,
        "type": "event",
        "inputs": [
            {
                "type": "address",
                "name": "src",
                "indexed": True,
                "internalType": "address"
            },
            {
                "type": "address",
                "internalType": "address",
                "indexed": True,
                "name": "guy"
            },
            {
                "name": "wad",
                "internalType": "uint256",
                "type": "uint256",
                "indexed": False
            }
        ],
        "name": "Approval"
    },
    {
        "inputs": [
            {
                "name": "dst",
                "internalType": "address",
                "indexed": True,
                "type": "address"
            },
            {
                "type": "uint256",
                "indexed": False,
                "name": "wad",
                "internalType": "uint256"
            }
        ],
        "name": "Deposit",
        "anonymous": False,
        "type": "event"
    },
    {
        "type": "event",
        "name": "Transfer",
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "src",
                "type": "address"
            },
            {
                "internalType": "address",
                "indexed": True,
                "type": "address",
                "name": "dst"
            },
            {
                "name": "wad",
                "internalType": "uint256",
                "type": "uint256",
                "indexed": False
            }
        ]
    },
    {
        "type": "event",
        "inputs": [
            {
                "type": "address",
                "indexed": True,
                "internalType": "address",
                "name": "src"
            },
            {
                "internalType": "uint256",
                "name": "wad",
                "type": "uint256",
                "indexed": False
            }
        ],
        "name": "Withdrawal",
        "anonymous": False
    },
    {
        "inputs": [
            {
                "name": "",
                "type": "address",
                "internalType": "address"
            },
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "type": "function",
        "name": "allowance",
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
        "name": "balanceOf",
        "type": "function",
        "outputs": [
            {
                "type": "uint256",
                "internalType": "uint256",
                "name": ""
            }
        ],
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
        "name": "decimals",
        "stateMutability": "view",
        "outputs": [
            {
                "name": "",
                "internalType": "uint8",
                "type": "uint8"
            }
        ],
        "inputs": [],
        "constant": True,
        "signature": "0x313ce567"
    },
    {
        "inputs": [],
        "name": "name",
        "type": "function",
        "stateMutability": "view",
        "outputs": [
            {
                "type": "string",
                "internalType": "string",
                "name": ""
            }
        ],
        "constant": True,
        "signature": "0x06fdde03"
    },
    {
        "stateMutability": "view",
        "inputs": [],
        "name": "symbol",
        "type": "function",
        "outputs": [
            {
                "internalType": "string",
                "type": "string",
                "name": ""
            }
        ],
        "constant": True,
        "signature": "0x95d89b41"
    },
    {
        "type": "receive",
        "stateMutability": "payable"
    },
    {
        "inputs": [],
        "stateMutability": "payable",
        "outputs": [],
        "name": "deposit",
        "type": "function"
    },
    {
        "outputs": [],
        "name": "withdraw",
        "type": "function",
        "stateMutability": "nonpayable",
        "inputs": [
            {
                "type": "uint256",
                "name": "wad",
                "internalType": "uint256"
            }
        ]
    },
    {
        "stateMutability": "view",
        "name": "totalSupply",
        "inputs": [],
        "outputs": [
            {
                "name": "",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "type": "function",
        "constant": True,
        "signature": "0x18160ddd"
    },
    {
        "name": "approve",
        "type": "function",
        "inputs": [
            {
                "internalType": "address",
                "type": "address",
                "name": "guy"
            },
            {
                "name": "wad",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "nonpayable"
    },
    {
        "name": "transfer",
        "type": "function",
        "outputs": [
            {
                "internalType": "bool",
                "type": "bool",
                "name": ""
            }
        ],
        "inputs": [
            {
                "name": "dst",
                "type": "address",
                "internalType": "address"
            },
            {
                "type": "uint256",
                "name": "wad",
                "internalType": "uint256"
            }
        ],
        "stateMutability": "nonpayable"
    },
    {
        "type": "function",
        "name": "transferFrom",
        "inputs": [
            {
                "type": "address",
                "internalType": "address",
                "name": "src"
            },
            {
                "type": "address",
                "name": "dst",
                "internalType": "address"
            },
            {
                "name": "wad",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "stateMutability": "nonpayable",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ]
    }
]

w3 = Web3(Web3.HTTPProvider(settings.RPC_ADDRESS))

CONTRACT = w3.eth.contract(Web3.toChecksumAddress(CONTRACT_ADDRESS), abi=ABI)
