// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC1155/IERC1155.sol";

contract GenieSend {

    struct Erc721Transfer {
        address erc721;
        address[] recipients;
        uint[] tokenIds;
    }

    struct Erc1155Transfer {
        address erc1155;
        address[] recipients;
        uint[] tokenIds;
        uint[] quantities;
    }

    constructor() {}

    function multisend(
        Erc721Transfer[] calldata erc721transfers,
        Erc1155Transfer[] calldata erc1155transfers
    ) public {
        for (uint i=0; i < erc721transfers.length; i++) {
            require(
                erc721transfers[i].recipients.length == erc721transfers[i].tokenIds.length,
                "Mismatched recipients and tokenIds length in ERC 721"
            );
            for (uint j=0; j < erc721transfers[i].recipients.length; j++) {
                IERC721(erc721transfers[i].erc721).safeTransferFrom(
                    msg.sender,
                    erc721transfers[i].recipients[j],
                    erc721transfers[i].tokenIds[j]
                );
            }
        }
        for (uint i=0; i < erc1155transfers.length; i++) {
            require(
                erc1155transfers[i].recipients.length == erc1155transfers[i].tokenIds.length,
                "Mismatched recipients and tokenIds length in ERC 1155"
            );
            for (uint j=0; j < erc1155transfers[i].recipients.length; j++) {
                IERC1155(erc1155transfers[i].erc1155).safeTransferFrom(
                    msg.sender,
                    erc1155transfers[i].recipients[j],
                    erc1155transfers[i].tokenIds[j],
                    erc1155transfers[i].quantities[j],
                    ""
                );
            }
        }
    }
}