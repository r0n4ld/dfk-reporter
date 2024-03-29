from django.conf import settings
from web3 import Web3

CONTRACT_ADDRESS = '0x24ad62502d1C652Cc7684081169D04896aC20f30'

ABI = [
    {
        "stateMutability": "nonpayable",
        "type": "constructor",
        "inputs": [
            {
                "internalType": "address",
                "name": "_factory",
                "type": "address"
            },
            {
                "name": "_WETH",
                "type": "address",
                "internalType": "address"
            }
        ]
    },
    {
        "type": "function",
        "inputs": [],
        "name": "WETH",
        "stateMutability": "view",
        "outputs": [
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
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "inputs": [],
        "name": "factory"
    },
    {
        "type": "receive",
        "stateMutability": "payable"
    },
    {
        "stateMutability": "nonpayable",
        "inputs": [
            {
                "internalType": "address",
                "name": "tokenA",
                "type": "address"
            },
            {
                "name": "tokenB",
                "internalType": "address",
                "type": "address"
            },
            {
                "type": "uint256",
                "name": "amountADesired",
                "internalType": "uint256"
            },
            {
                "name": "amountBDesired",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "name": "amountAMin",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "name": "amountBMin",
                "internalType": "uint256",
                "type": "uint256"
            },
            {
                "name": "to",
                "internalType": "address",
                "type": "address"
            },
            {
                "type": "uint256",
                "name": "deadline",
                "internalType": "uint256"
            }
        ],
        "outputs": [
            {
                "name": "amountA",
                "internalType": "uint256",
                "type": "uint256"
            },
            {
                "type": "uint256",
                "name": "amountB",
                "internalType": "uint256"
            },
            {
                "name": "liquidity",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "name": "addLiquidity",
        "type": "function"
    },
    {
        "name": "addLiquidityETH",
        "type": "function",
        "outputs": [
            {
                "name": "amountToken",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "name": "amountETH",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "name": "liquidity",
                "internalType": "uint256",
                "type": "uint256"
            }
        ],
        "inputs": [
            {
                "type": "address",
                "internalType": "address",
                "name": "token"
            },
            {
                "name": "amountTokenDesired",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "type": "uint256",
                "internalType": "uint256",
                "name": "amountTokenMin"
            },
            {
                "type": "uint256",
                "internalType": "uint256",
                "name": "amountETHMin"
            },
            {
                "type": "address",
                "internalType": "address",
                "name": "to"
            },
            {
                "name": "deadline",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "stateMutability": "payable"
    },
    {
        "name": "removeLiquidity",
        "outputs": [
            {
                "name": "amountA",
                "internalType": "uint256",
                "type": "uint256"
            },
            {
                "type": "uint256",
                "name": "amountB",
                "internalType": "uint256"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function",
        "inputs": [
            {
                "internalType": "address",
                "type": "address",
                "name": "tokenA"
            },
            {
                "name": "tokenB",
                "internalType": "address",
                "type": "address"
            },
            {
                "type": "uint256",
                "name": "liquidity",
                "internalType": "uint256"
            },
            {
                "name": "amountAMin",
                "internalType": "uint256",
                "type": "uint256"
            },
            {
                "name": "amountBMin",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "type": "address",
                "internalType": "address",
                "name": "to"
            },
            {
                "type": "uint256",
                "name": "deadline",
                "internalType": "uint256"
            }
        ]
    },
    {
        "name": "removeLiquidityETH",
        "type": "function",
        "inputs": [
            {
                "name": "token",
                "internalType": "address",
                "type": "address"
            },
            {
                "name": "liquidity",
                "internalType": "uint256",
                "type": "uint256"
            },
            {
                "name": "amountTokenMin",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amountETHMin",
                "type": "uint256"
            },
            {
                "name": "to",
                "internalType": "address",
                "type": "address"
            },
            {
                "type": "uint256",
                "internalType": "uint256",
                "name": "deadline"
            }
        ],
        "outputs": [
            {
                "type": "uint256",
                "internalType": "uint256",
                "name": "amountToken"
            },
            {
                "internalType": "uint256",
                "name": "amountETH",
                "type": "uint256"
            }
        ],
        "stateMutability": "nonpayable"
    },
    {
        "stateMutability": "nonpayable",
        "name": "removeLiquidityWithPermit",
        "type": "function",
        "outputs": [
            {
                "name": "amountA",
                "internalType": "uint256",
                "type": "uint256"
            },
            {
                "name": "amountB",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "inputs": [
            {
                "internalType": "address",
                "name": "tokenA",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "tokenB",
                "type": "address"
            },
            {
                "name": "liquidity",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "type": "uint256",
                "internalType": "uint256",
                "name": "amountAMin"
            },
            {
                "internalType": "uint256",
                "type": "uint256",
                "name": "amountBMin"
            },
            {
                "type": "address",
                "name": "to",
                "internalType": "address"
            },
            {
                "internalType": "uint256",
                "type": "uint256",
                "name": "deadline"
            },
            {
                "internalType": "bool",
                "name": "approveMax",
                "type": "bool"
            },
            {
                "type": "uint8",
                "internalType": "uint8",
                "name": "v"
            },
            {
                "name": "r",
                "internalType": "bytes32",
                "type": "bytes32"
            },
            {
                "type": "bytes32",
                "internalType": "bytes32",
                "name": "s"
            }
        ]
    },
    {
        "stateMutability": "nonpayable",
        "name": "removeLiquidityETHWithPermit",
        "type": "function",
        "outputs": [
            {
                "type": "uint256",
                "name": "amountToken",
                "internalType": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amountETH",
                "type": "uint256"
            }
        ],
        "inputs": [
            {
                "name": "token",
                "type": "address",
                "internalType": "address"
            },
            {
                "name": "liquidity",
                "internalType": "uint256",
                "type": "uint256"
            },
            {
                "type": "uint256",
                "internalType": "uint256",
                "name": "amountTokenMin"
            },
            {
                "name": "amountETHMin",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "deadline",
                "type": "uint256"
            },
            {
                "internalType": "bool",
                "name": "approveMax",
                "type": "bool"
            },
            {
                "name": "v",
                "type": "uint8",
                "internalType": "uint8"
            },
            {
                "name": "r",
                "type": "bytes32",
                "internalType": "bytes32"
            },
            {
                "type": "bytes32",
                "internalType": "bytes32",
                "name": "s"
            }
        ]
    },
    {
        "type": "function",
        "inputs": [
            {
                "type": "address",
                "name": "token",
                "internalType": "address"
            },
            {
                "name": "liquidity",
                "internalType": "uint256",
                "type": "uint256"
            },
            {
                "type": "uint256",
                "name": "amountTokenMin",
                "internalType": "uint256"
            },
            {
                "name": "amountETHMin",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "type": "address",
                "name": "to",
                "internalType": "address"
            },
            {
                "name": "deadline",
                "internalType": "uint256",
                "type": "uint256"
            }
        ],
        "name": "removeLiquidityETHSupportingFeeOnTransferTokens",
        "outputs": [
            {
                "type": "uint256",
                "internalType": "uint256",
                "name": "amountETH"
            }
        ],
        "stateMutability": "nonpayable"
    },
    {
        "outputs": [
            {
                "name": "amountETH",
                "internalType": "uint256",
                "type": "uint256"
            }
        ],
        "name": "removeLiquidityETHWithPermitSupportingFeeOnTransferTokens",
        "stateMutability": "nonpayable",
        "type": "function",
        "inputs": [
            {
                "internalType": "address",
                "name": "token",
                "type": "address"
            },
            {
                "type": "uint256",
                "internalType": "uint256",
                "name": "liquidity"
            },
            {
                "name": "amountTokenMin",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "type": "uint256",
                "internalType": "uint256",
                "name": "amountETHMin"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "name": "deadline",
                "internalType": "uint256",
                "type": "uint256"
            },
            {
                "name": "approveMax",
                "type": "bool",
                "internalType": "bool"
            },
            {
                "internalType": "uint8",
                "name": "v",
                "type": "uint8"
            },
            {
                "type": "bytes32",
                "internalType": "bytes32",
                "name": "r"
            },
            {
                "type": "bytes32",
                "internalType": "bytes32",
                "name": "s"
            }
        ]
    },
    {
        "type": "function",
        "stateMutability": "nonpayable",
        "name": "swapExactTokensForTokens",
        "outputs": [
            {
                "name": "amounts",
                "internalType": "uint256[]",
                "type": "uint256[]"
            }
        ],
        "inputs": [
            {
                "type": "uint256",
                "name": "amountIn",
                "internalType": "uint256"
            },
            {
                "type": "uint256",
                "name": "amountOutMin",
                "internalType": "uint256"
            },
            {
                "type": "address[]",
                "internalType": "address[]",
                "name": "path"
            },
            {
                "type": "address",
                "name": "to",
                "internalType": "address"
            },
            {
                "type": "uint256",
                "internalType": "uint256",
                "name": "deadline"
            }
        ]
    },
    {
        "type": "function",
        "stateMutability": "nonpayable",
        "outputs": [
            {
                "type": "uint256[]",
                "internalType": "uint256[]",
                "name": "amounts"
            }
        ],
        "name": "swapTokensForExactTokens",
        "inputs": [
            {
                "name": "amountOut",
                "internalType": "uint256",
                "type": "uint256"
            },
            {
                "name": "amountInMax",
                "internalType": "uint256",
                "type": "uint256"
            },
            {
                "name": "path",
                "type": "address[]",
                "internalType": "address[]"
            },
            {
                "type": "address",
                "name": "to",
                "internalType": "address"
            },
            {
                "type": "uint256",
                "name": "deadline",
                "internalType": "uint256"
            }
        ]
    },
    {
        "stateMutability": "payable",
        "inputs": [
            {
                "type": "uint256",
                "name": "amountOutMin",
                "internalType": "uint256"
            },
            {
                "type": "address[]",
                "name": "path",
                "internalType": "address[]"
            },
            {
                "type": "address",
                "name": "to",
                "internalType": "address"
            },
            {
                "type": "uint256",
                "name": "deadline",
                "internalType": "uint256"
            }
        ],
        "outputs": [
            {
                "name": "amounts",
                "type": "uint256[]",
                "internalType": "uint256[]"
            }
        ],
        "name": "swapExactETHForTokens",
        "type": "function"
    },
    {
        "outputs": [
            {
                "internalType": "uint256[]",
                "type": "uint256[]",
                "name": "amounts"
            }
        ],
        "name": "swapTokensForExactETH",
        "stateMutability": "nonpayable",
        "type": "function",
        "inputs": [
            {
                "name": "amountOut",
                "internalType": "uint256",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amountInMax",
                "type": "uint256"
            },
            {
                "type": "address[]",
                "internalType": "address[]",
                "name": "path"
            },
            {
                "type": "address",
                "internalType": "address",
                "name": "to"
            },
            {
                "type": "uint256",
                "name": "deadline",
                "internalType": "uint256"
            }
        ]
    },
    {
        "type": "function",
        "outputs": [
            {
                "name": "amounts",
                "internalType": "uint256[]",
                "type": "uint256[]"
            }
        ],
        "stateMutability": "nonpayable",
        "name": "swapExactTokensForETH",
        "inputs": [
            {
                "type": "uint256",
                "internalType": "uint256",
                "name": "amountIn"
            },
            {
                "name": "amountOutMin",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "type": "address[]",
                "name": "path",
                "internalType": "address[]"
            },
            {
                "type": "address",
                "name": "to",
                "internalType": "address"
            },
            {
                "name": "deadline",
                "internalType": "uint256",
                "type": "uint256"
            }
        ]
    },
    {
        "name": "swapETHForExactTokens",
        "outputs": [
            {
                "name": "amounts",
                "type": "uint256[]",
                "internalType": "uint256[]"
            }
        ],
        "type": "function",
        "stateMutability": "payable",
        "inputs": [
            {
                "name": "amountOut",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "type": "address[]",
                "name": "path",
                "internalType": "address[]"
            },
            {
                "name": "to",
                "type": "address",
                "internalType": "address"
            },
            {
                "internalType": "uint256",
                "type": "uint256",
                "name": "deadline"
            }
        ]
    },
    {
        "stateMutability": "nonpayable",
        "outputs": [],
        "inputs": [
            {
                "name": "amountIn",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "type": "uint256",
                "internalType": "uint256",
                "name": "amountOutMin"
            },
            {
                "name": "path",
                "internalType": "address[]",
                "type": "address[]"
            },
            {
                "internalType": "address",
                "type": "address",
                "name": "to"
            },
            {
                "name": "deadline",
                "internalType": "uint256",
                "type": "uint256"
            }
        ],
        "name": "swapExactTokensForTokensSupportingFeeOnTransferTokens",
        "type": "function"
    },
    {
        "inputs": [
            {
                "name": "amountOutMin",
                "internalType": "uint256",
                "type": "uint256"
            },
            {
                "internalType": "address[]",
                "type": "address[]",
                "name": "path"
            },
            {
                "type": "address",
                "name": "to",
                "internalType": "address"
            },
            {
                "name": "deadline",
                "internalType": "uint256",
                "type": "uint256"
            }
        ],
        "name": "swapExactETHForTokensSupportingFeeOnTransferTokens",
        "type": "function",
        "outputs": [],
        "stateMutability": "payable"
    },
    {
        "name": "swapExactTokensForETHSupportingFeeOnTransferTokens",
        "stateMutability": "nonpayable",
        "type": "function",
        "inputs": [
            {
                "internalType": "uint256",
                "name": "amountIn",
                "type": "uint256"
            },
            {
                "name": "amountOutMin",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "type": "address[]",
                "internalType": "address[]",
                "name": "path"
            },
            {
                "type": "address",
                "name": "to",
                "internalType": "address"
            },
            {
                "internalType": "uint256",
                "type": "uint256",
                "name": "deadline"
            }
        ],
        "outputs": []
    },
    {
        "inputs": [
            {
                "name": "amountA",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "name": "reserveA",
                "internalType": "uint256",
                "type": "uint256"
            },
            {
                "name": "reserveB",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "outputs": [
            {
                "name": "amountB",
                "internalType": "uint256",
                "type": "uint256"
            }
        ],
        "stateMutability": "pure",
        "name": "quote",
        "type": "function"
    },
    {
        "outputs": [
            {
                "name": "amountOut",
                "internalType": "uint256",
                "type": "uint256"
            }
        ],
        "type": "function",
        "name": "getAmountOut",
        "inputs": [
            {
                "type": "uint256",
                "name": "amountIn",
                "internalType": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "reserveIn",
                "type": "uint256"
            },
            {
                "type": "uint256",
                "internalType": "uint256",
                "name": "reserveOut"
            }
        ],
        "stateMutability": "pure"
    },
    {
        "outputs": [
            {
                "internalType": "uint256",
                "type": "uint256",
                "name": "amountIn"
            }
        ],
        "name": "getAmountIn",
        "type": "function",
        "inputs": [
            {
                "name": "amountOut",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "reserveIn",
                "type": "uint256"
            },
            {
                "type": "uint256",
                "internalType": "uint256",
                "name": "reserveOut"
            }
        ],
        "stateMutability": "pure"
    },
    {
        "type": "function",
        "stateMutability": "view",
        "outputs": [
            {
                "name": "amounts",
                "internalType": "uint256[]",
                "type": "uint256[]"
            }
        ],
        "name": "getAmountsOut",
        "inputs": [
            {
                "name": "amountIn",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "name": "path",
                "internalType": "address[]",
                "type": "address[]"
            }
        ]
    },
    {
        "name": "getAmountsIn",
        "type": "function",
        "inputs": [
            {
                "name": "amountOut",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "internalType": "address[]",
                "type": "address[]",
                "name": "path"
            }
        ],
        "outputs": [
            {
                "name": "amounts",
                "type": "uint256[]",
                "internalType": "uint256[]"
            }
        ],
        "stateMutability": "view"
    }
]

w3 = Web3(Web3.HTTPProvider(settings.RPC_ADDRESS))

CONTRACT = w3.eth.contract(Web3.toChecksumAddress(CONTRACT_ADDRESS), abi=ABI)
