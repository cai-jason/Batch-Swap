from brownie import MyErc721, accounts, config, network

def main():
    acct1 = accounts.add(
        config["wallets"]["from_key"]
    )
    acct2 = accounts.add(
        config["wallets"]["from_key_2"]
    )
    acct3 = accounts.add(
        config["wallets"]["from_key_3"]
    )

    # myErc721 = MyErc721.deploy(
    #     'name',
    #     'symbol',
    #     1,
    #     {"from": acct1}
    # )
    myErc721 = MyErc721[-1]
    myErc721.setIndex(10, {'from': acct1})

    myErc721.mintTokens({'from': acct1})
    for i in range(0, 10):
        myErc721.safeTransferFrom(
            acct1,
            acct2,
            i,
            "",
            {'from': acct1}
        )

    for i in range(0, 10):
        myErc721.safeTransferFrom(
            acct2,
            acct1,
            i,
            "",
            {'from': acct2}
        )
    myErc721.burnTokens({'from': acct1})

    return myErc721
