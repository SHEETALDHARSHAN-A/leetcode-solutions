# Write your MySQL query statement below
SELECT 
    Person.firstName AS FirstName,
    Person.lastName AS LastName,
    Address.city AS City,
    Address.state AS State
FROM
    Person
LEFT JOIN
    Address
ON
    Person.personid = Address.personid
