from brownie import MyErc721, accounts, config, network

def main():
    acct1 = accounts.add(
        config["wallets"]["from_key"]
    )
    acct2 = accounts.add(
        config["wallets"]["from_key_2"]
    )

    # myErc721 = MyErc721.deploy(
    #     'name',
    #     'symbol',
    #     1,
    #     {"from": acct1}
    # )
    myErc721 = MyErc721[-1]
    myErc721.setIndex(100, {'from': acct1})

    myErc721.mintTokens({'from': acct1})
    myErc721.sendTokens(
        acct2,
        {'from': acct1}
    )
    myErc721.sendTokens(
        acct1,
        {'from': acct2}
    )
    myErc721.burnTokens({'from': acct1})

    return myErc721
