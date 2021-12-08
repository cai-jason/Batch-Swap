// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";

contract MyErc1155 is ERC1155 {
    constructor() public ERC1155("") {
    }
}
