from NetGuard.contract_config import *
from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware

class Contract:
    def __init__(self, rpc_url, contract_address, contract_abi):
        try:
            self.web3 =  Web3(Web3.HTTPProvider(rpc_url))
            self.web3.middleware_onion.inject(geth_poa_middleware, layer=0)
            self.instance = self.web3.eth.contract(address=self.web3.toChecksumAddress(contract_address),
                                                   abi=contract_abi)
        except Exception as e:
            raise str(e)
    
    def unlock(self, coinbase_account, password, expiry=3600):
        try:
            return self.web3.geth.personal.unlockAccount(coinbase_account, password, expiry)
        except Exception as e:
            return str(e)
    
    def getAddress(self, private_key):
        try:
            return self.web3.eth.account.privateKeyToAccount(private_key)
        except Exception as e:
            return str(e)


class NetGuard_Ideathon:
    def __init__(self, contract):
        self.contract = contract
    
    def create(self, content, domain):
        try:
            checkerDetails = self.contract.instance.functions.addCheckerDetail(content, domain)
            trans = {"nonce":contract.web3.eth.getTransactionCount(acct.address), "from":acct.address, "to":contract_address, "gas":800000, "gasPrice":contract.web3.toWei("21", "gwei")}
            signed = acct.signTransaction(trans)
            transaction_hash = contract.web3.eth.sendRawTransaction(signed.rawTransaction)
            return transaction_hash
        except Exception as e:
            return str(e)
    
    def getValues(self, domain):
        try:
            data = contract.instance.functions.CheckerDetails("facebook.com").call()
            return {"spam": data[0], "adv":data[1], "spyware":data[2], "malware":data[3], "safe":data[4]}
        except Exception as e:
            return str(e)
            

