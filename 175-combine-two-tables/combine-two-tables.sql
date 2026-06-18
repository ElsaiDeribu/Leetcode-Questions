-- Write your PostgreSQL query statement below
select 
    p.firstName, 
    p.lastName, 
    a.city, 
    a.state 
From Person p
Left Join Address a 
on p.personID = a.personID