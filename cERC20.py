import json
import pkg_resources

from typing import Optional
from web3 import Web3

from compoundv2 import account, Address, Contract
from compoundv2.cToken import cToken
from compoundv2.transactor import Transactor

class cERC20(cToken):
    """
    Python wrapper for Compound 'Presidio' v2's cERC20 Solidity Smart Contract
    """

    #TODO: fix this to include the ABI JSON for whatever contract being used
    #abi = Contract._retrieve_abi(__name__, 'abi/' + self.__class__.__name__ + '.json')

    def __init__(
            self, 
            web3: Web3, 
            address: Address, 
            sender: Address,
            abi: str
    ):
        assert(isinstance(web3, Web3))
        assert(isinstance(address, Address))
        assert(isinstance(sender, Address))
        assert(isinstance(abi, str))

        self.web3       = web3
        self.address    = address
        self.sender     = sender
        # the ERC20 contract is different here, the ABI must be provided
        self.abi        = Contract._retrieve_abi(__name__, abi)
        self._contract  = self._get_contract(web3, self.abi, address)

    def mint(
            self, 
            amountToMint: int
    ):
        """
        TBU
        """
        return Transactor(
            self.web3, 
            self.address, 
            self._contract, 
            'mint',
            [self.web3.toWei(amountToMint, 'ether')]
        )

    def redeem(
            self, 
            redeemAmount: int
    ):
        return Transactor(
            self.web3,
            self.address,
            self._contract,
            'redeem',
            [redeemAmount]
        )

    def redeemUnderlying(self, redeemAmount):
        """
        TBU
        """
        return Transactor(
            self.web3,
            self.address,
            self._contract,
            'redeemUnderlying',
            [redeemAmount]
        )

    def borrow(self, borrowAmount):
        """
        TBU
        """
        return Transactor(
            self.web3,
            self.address,
            self._contract,
            'borrow',
            [borrowAmount] 
        )

    def repayBorrow(self, repayAmount):
        """
        TBU
        """
        return Transactor(
            self.web3,
            self.address,
            self._contract,
            'repayBorrow',
            [repayAmount]
        )

    def repayBorrowBehalf(
            self, 
            addressBorrower: str, 
            repayAmount: int
    ):
        """
        TBU
        """
        return Transactor(
            self.web3,
            self.address,
            self._contract,
            'repayBorrowBehalf',
            [addressBorrower, repayAmount]
        )

    def liquidateBorrow(
            self, 
            addressBorrower, 
            repayAmount, 
            addressCTokenCollateral
    ):
        """
        TBU
        """
        return Transactor(
            self.web3,
            self.address,
            self._contract,
            'liquidateBorrow',
            [addressBorrower, repayAmount, addessCTokenCollateral]
        )

