// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {
    // Structure to hold student details
    struct Student {
        uint id;
        string name;
        uint age;
    }

    // Array to store students
    Student[] public students;
    uint public studentCount = 0;

    // Function to add a student
    function addStudent(string memory _name, uint _age) public {
        students.push(Student(studentCount, _name, _age));
        studentCount++;
    }

    // Function to get student by ID
    function getStudent(uint _id) public view returns (string memory, uint) {
        require(_id < studentCount, "Student does not exist.");
        Student memory student = students[_id];
        return (student.name, student.age);
    }

    // Fallback function to handle unexpected calls
    fallback() external payable {}

    // Receive function to accept Ether
    receive() external payable {}
}
