-- #SQL50
-- Employee Bonus - LeetCode
-- https://leetcode.com/problems/employee-bonus/submissions/1176026081/?envType=study-plan-v2&envId=top-sql-50

select
  e.name
  , b.bonus
from
  Employee e
  left join Bonus b on e.empId = b.empId
where
  b.bonus < 1000
  or b.bonus is null
;

-- Example 1:
-- SELECT Employee.name,Bonus.bonus FROM Employee
-- LEFT JOIN Bonus ON Employee.empID = Bonus.empID
-- WHERE bonus < 1000 OR Bonus IS NULL ;
