from brownie import GenieSend, MyErc721, MyErc1155, accounts, config, network

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

    # genie_send = GenieSend.deploy(
    #     {"from": acct1}
    # )
    genie_send = GenieSend[-1]
    my_erc721 = MyErc721[-1]
    my_erc1155 = MyErc1155[-1]
    network.priority_fee('1.2 gwei')

    my_erc721.setIndex(10, {'from': acct1})
    my_erc721.mintTokens({'from': acct1})    
    my_erc721.setApprovalForAll(genie_send, True, {'from': acct1})

    my_erc1155.setApprovalForAll(genie_send, True, {'from': acct1})

    recipients = [ acct2 ] * 10 
    token_ids = list(range(10))

    erc721_transfer = [(
        my_erc721,
        recipients,
        token_ids
    )]
    genie_send.multisend(
        erc721_transfer, 
        [],
        {'from': acct1}
    )

    recipients = [ acct1 ] * 10 
    token_ids = list(range(10))

    my_erc721.setApprovalForAll(genie_send, True, {'from': acct2})

    erc721_transfer = [(
        my_erc721,
        recipients,
        token_ids
    )]
    genie_send.multisend(
        erc721_transfer, 
        [],
        {'from': acct2}
    )

    return genie_send
