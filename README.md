# pycompoundv2
### Python wrapper for Compound v2 'Presidio'

Currently, config variables are retrieved from a 'config.ini' file. 

Quick example of how this works:

```
import configparser
from web3 import Web3
from compoundv2 import Address
from compoundv2.cDAI import cDAI

def main():
    get_balance_call = cdai_contract.balanceOf(my_address)
    print(get_balance_call)

if __name__ == '__main__':
    # config 
    config = configparser.ConfigParser()
    config.read('config.ini')

    # infura endpoint
    infura_rinkeby = config['PROVIDER']['InfuraRinkeby']

    # web3
    web3 = Web3(Web3.HTTPProvider(infura_rinkeby))

    # keys and accounts
    private_key = config['ACCOUNT']['PrivateKey']
    my_address = Address(config['ACCOUNT']['Address'])

    # cDai cERC20 address and contract
    cdai_address = Address(config['COMPOUND-CONTRACTS']['cDAI'])
    cdai_contract = cDAI(web3, cdai_address, my_address)    
    main()

```
