// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract MyErc721 is ERC721 {
	uint256 index;
    constructor(string memory name_, string memory symbol_, uint256 index_) public ERC721(name_, symbol_) {
    	index = index_;
    }

    function setIndex(uint256 index_) public {
    	index = index_;
    }

    function mintTokens() public {
    	for (uint i=0; i<index; i++) {
    		_safeMint(msg.sender, i);
    	}
    }

    function burnTokens() public {
    	for (uint i=0; i<index; i++) {
    		_burn(i);
    	}
    }

    function sendTokens(address to_, uint256 index_) public {
		safeTransferFrom(
			msg.sender,
			to_,
			index_,
			""
		);
    }
}
