-- Write your PostgreSQL query statement below

select name
from Customer c
where c.referee_id != 2 or c.referee_id is null