from brownie import MockV3Aggregator, config, network, accounts, FundMe
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHIANS_ENV,
    FORKED_LOCAL_ENV,
)
from web3 import Web3


def deploy_fund_me():
    account = get_account()
    print(account.address)
    print(network.show_active())
    ##pass the pricefeed address to fund me

    # if on persistent network

    if network.show_active() not in LOCAL_BLOCKCHIANS_ENV:
        # use chainlink aggregator
        priceFeedAdress = config["networks"][network.show_active()].get(
            "eth_usd_price_feed"
        )
        print(f" printed it {priceFeedAdress}")
    else:
        # deploy the Mock Aggregator contract to the local dev ganache chain
        deploy_mocks()
        priceFeedAdress = MockV3Aggregator[-1].address

    # Deploys the fundme contract to the chosen chain
    fund_me = FundMe.deploy(
        priceFeedAdress,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
