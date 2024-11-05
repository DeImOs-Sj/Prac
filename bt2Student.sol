// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;
contract MarksManagmtSys{
	struct Student{
		int ID;
		string fName;
		string lName;
		int marks;
	}

	address owner;
	int public stdCount = 0;
	mapping(int => Student) public stdRecords;

	function addNewRecords(int _ID, string memory _fName, string memory _lName, int _marks) public {
	    stdCount = stdCount + 1;
  
    	stdRecords[stdCount] = Student(_ID, _fName, _lName, _marks);
	}
}