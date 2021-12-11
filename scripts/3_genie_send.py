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

    network.priority_fee('1 gwei')
    # genie_send = GenieSend.deploy(
    #     {"from": acct1}
    # )
    genie_send = GenieSend[-1]
    my_erc721 = MyErc721[-1]
    my_erc1155 = MyErc1155[-1]

    # my_erc721.setIndex(10, {'from': acct1})
    # my_erc721.mintTokens({'from': acct1})    
    erc721_recipients = [ acct2 ] * 5 + [ acct3 ] * 5
    erc721_token_ids = list(range(10))
    erc721_transfer = [(
        my_erc721,
        erc721_recipients,
        erc721_token_ids
    )]
    my_erc721.setApprovalForAll(genie_send, True, {'from': acct1})

    erc1155_recipients = [ acct2 ] * 5 + [ acct3 ] * 5
    erc1155_token_ids = list(range(10))
    erc1155_quantities = [ 1 ] * 10
    erc1155_transfer = [(
        my_erc1155,
        erc1155_recipients,
        erc1155_token_ids,
        erc1155_quantities
    )]
    my_erc1155.setApprovalForAll(genie_send, True, {'from': acct1})

    genie_send.multisend(
        erc721_transfer, 
        erc1155_transfer,
        {'from': acct1}
    )

    erc721_recipients = [ acct1 ] * 5
    erc721_token_ids = list(range(5))
    erc721_transfer = [(
        my_erc721,
        erc721_recipients,
        erc721_token_ids
    )]
    my_erc721.setApprovalForAll(genie_send, True, {'from': acct2})

    erc1155_recipients = [ acct1 ] * 5
    erc1155_token_ids = list(range(5))
    erc1155_quantities = [ 1 ] * 5
    erc1155_transfer = [(
        my_erc1155,
        erc1155_recipients,
        erc1155_token_ids,
        erc1155_quantities
    )]
    my_erc1155.setApprovalForAll(genie_send, True, {'from': acct2})

    genie_send.multisend(
        erc721_transfer,
        erc1155_transfer,
        {'from': acct2}
    )

    erc721_recipients = [ acct1 ] * 5
    erc721_token_ids = list(range(5, 10))
    erc721_transfer = [(
        my_erc721,
        erc721_recipients,
        erc721_token_ids
    )]
    my_erc721.setApprovalForAll(genie_send, True, {'from': acct3})

    erc1155_recipients = [ acct1 ] * 5
    erc1155_token_ids = list(range(5, 10))
    erc1155_quantities = [ 1 ] * 5
    erc1155_transfer = [(
        my_erc1155,
        erc1155_recipients,
        erc1155_token_ids,
        erc1155_quantities
    )]
    my_erc1155.setApprovalForAll(genie_send, True, {'from': acct3})

    genie_send.multisend(
        erc721_transfer,
        erc1155_transfer,
        {'from': acct3}
    )

    return genie_send
