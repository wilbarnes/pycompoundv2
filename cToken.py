import json
import pkg_resources

from typing import Optional
from web3 import Web3

from compoundv2 import account, Address, Contract
from compoundv2.transactor import Transactor

class cToken(Contract):
    """
    cToken Helper functions for use in:
    - cETH
    - cERC20
    """

    def exchangeRateCurrent(self):
        return self._contract.call().exchangeRateCurrent()

    def getCash(self):
        return self._contract.call().getCash()

    def totalBorrowsCurrent(self):
        return self._contract.call().totalBorrowsCurrent()

    def borrowBalanceCurrent(self, addressToCheck: Address):
        return self._contract.call().borrowBalanceCurrent(addressToCheck)

    def borrowRatePerBlock(self):
        return self._contract.call().borrowRatePerBlock()

    def totalSupply(self):
        return self._contract.call().totalSupply()

    def balanceOf(self, addressToCheck: Address):
        return self._contract.call().balanceOf(addressToCheck)

    def supplyRatePerBlock(self):
        return self._contract.call().supplyRatePerBlock()

    def totalReserves(self):
        return self._contract.call().totalReserves()

    def reserveFactorMantissa(self):
        return self._contract.call().reserveFactorMantissa()
