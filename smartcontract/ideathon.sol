pragma solidity ^0.6.12;
pragma experimental ABIEncoderV2;

contract ideathon{
    
    struct WebsiteChecker {  
        uint spam;
        uint adv;
        uint spyware;
        uint bot;
        uint safe;
    }
    
    string[] _DomainList;
    
    
    mapping (string => WebsiteChecker) public CheckerDetails;

    function addCheckerDetail (string calldata _Content, string calldata _DomainName) public returns(bool) {
        
        _DomainList.push(_DomainName);
        
        if (keccak256(abi.encodePacked((_Content))) == keccak256(abi.encodePacked(("spam")))){
            CheckerDetails[_DomainName].spam += 1;
        } else if (keccak256(abi.encodePacked((_Content))) == keccak256(abi.encodePacked(("adv")))){
            CheckerDetails[_DomainName].adv += 1;
        } else if (keccak256(abi.encodePacked((_Content))) == keccak256(abi.encodePacked(("spyware")))){
            CheckerDetails[_DomainName].spyware += 1;
        } else if (keccak256(abi.encodePacked((_Content))) == keccak256(abi.encodePacked(("bot")))){
            CheckerDetails[_DomainName].bot += 1;
        } else {
            CheckerDetails[_DomainName].safe += 1;
        }
    
        return true;
    }
    
    function getDomainList() public view returns (string[] memory){
        return _DomainList;
    }
    
    
}
