from decimal import Decimal
from brownie import config, accounts, network, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENV = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHIANS_ENV = ["development", "ganache-local"]
DECIMALS = 8
STARTING_PRICE = 20000000000


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHIANS_ENV
        or network.show_active() in FORKED_LOCAL_ENV
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print(f"Deploying Mocks")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
        print("Mocks deployed")
