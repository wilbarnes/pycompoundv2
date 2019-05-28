import os
from eth_account import Account
from web3 import Web3
from typing import Optional

def private_key_to_account(web3: Web3):
    private_key = os.environ['ETH_PRIVATE_KEY']
    account = Account.privateKeyToAccount(private_key)
    return account

class AccountManager:

    def __init__(self, web3: Web3):
        self.web3 = web3
        self.accounts = []

        assert(isinstance(web3, Web3))

    def list_accounts(self):
        return self.web3.personal.listAccounts

    def unlock_account(self, addressToUnlock, passphrase):
        return self.web3.personal.unlockAccount(addressToUnlock, passphrase)

