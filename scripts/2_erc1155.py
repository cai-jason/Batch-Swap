from brownie import MyErc1155, accounts, config, network

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

    network.priority_fee('1 gwei')
    # myErc1155 = MyErc1155.deploy(
    #     {"from": acct1}
    # )
    myErc1155 = MyErc1155[-1]
    for i in range(0, 10):
        myErc1155.safeTransferFrom(
            acct1,
            acct2,
            i,
            1,
            "",
            {'from': acct1}
        )
    for i in range(0, 10):
        myErc1155.safeTransferFrom(
            acct2,
            acct1,
            i,
            1,
            "",
            {'from': acct2}
        )

    return myErc1155
