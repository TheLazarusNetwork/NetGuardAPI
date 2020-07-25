contract_address = "0xdC34BaF6Cc8fC8c659b0d2E8933d704a11E41464"

private_key = "1849df47d56e75f323693931b6d27e3fb4e283cfc169546a5d83dbeeb272a221"

rpc_url = "https://goerli.infura.io/v3/9be13ca022e44fb7b7835bbc98fc5697"

contract_abi = [
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_Content",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_DomainName",
				"type": "string"
			}
		],
		"name": "addCheckerDetail",
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
		"inputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"name": "CheckerDetails",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "spam",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "adv",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "spyware",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "bot",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "safe",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getDomainList",
		"outputs": [
			{
				"internalType": "string[]",
				"name": "",
				"type": "string[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]