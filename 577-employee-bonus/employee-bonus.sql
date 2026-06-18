-- Write your PostgreSQL query statement below
Select
    e.name,
    b.bonus
From Employee e
Left Join Bonus b 
    on e.empId = b.empId
Where b.bonus < 1000 or b.bonus is null

