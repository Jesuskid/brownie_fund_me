# brownie_fund_me
Ethereum Solidity Brownie Smart Contract
A simple Ethereum smart contract that accepts eth from funders and allows the only owner of
the contract to withdraw funds.

### Features:
Allows any one to fund the contract with eth with amounts above or equal to $50 worth of eth
Allows only the owner of the contracts to deploy funds

N:B This contract makes use of the the chainlink price aggrgator to allow the contract to get the current ETH/USD value
