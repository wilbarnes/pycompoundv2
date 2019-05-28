import json
import pkg_resources

from typing import Optional
from web3 import Web3

from compoundv2 import account, Address, Contract
from compoundv2.transactor import Transactor

class cDAI(Contract):
    """
    Python wrapper for Compound 'Presidio' v2's cDAI Solidity Smart Contract
    """

    abi = Contract._retrieve_abi(__name__, 'abi/cDAI.json')

    def __init__(self, web3: Web3, address: Address, sender: Address):
        assert(isinstance(web3, Web3))
        assert(isinstance(address, Address))
        assert(isinstance(sender, Address))

        self.web3 = web3
        self.address = address
        self.sender = sender
        self._contract = self._get_contract(web3, self.abi, address)

    def mint(self, amountToMint):
        function_name = 'mint'

        # cDAI accepts amount to mint as a param, not as tx 'value'
        params = []
        params.append(int(self.web3.toWei(amountToMint, 'ether')))

        return Transactor(
            self.web3, 
            self.address, 
            self._contract, 
            function_name,
            params
        )

    def redeem(self, amountToRedeem):
        function_name = 'redeem'

        params = []
        params.append(int(amountToRedeem))

        return Transactor(
            self.web3,
            self.address,
            self._contract,
            function_name,
            params
        )

    def redeemUnderlying(self, amountToRedeem):
        function_name = 'redeem'

        params = []
        params.append(int(amountToRedeem))

        return Transactor(
            self.web3,
            self.address,
            self._contract,
            function_name,
            params
        )

    def balanceOf(self, addressToCheck):
        """
        Retrieve DAI balance of address provided
        """
        return self._contract.call().balanceOf(str(addressToCheck))

    def tokenWorth(self, addressToCheck):
        """
        Retrieve worth of tokens
        """
        return self._contract.call().balanceOf(str(addressToCheck)) * \
            self._contract.call().exchangeRateCurrent()

    def supplyRatePerBlock(self):
        """
        TBU
        """
        return self._contract.call().supplyRatePerBlock()

    def exchangeRateCurrent(self):
        """
        TBU
        """
        return self._contract.call().exchangeRateCurrent()
