-- #SQL50
-- Managers with at Least 5 Direct Reports - LeetCode
-- https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/?envType=study-plan-v2&envId=top-sql-50

-- Example 1:
Select m.name
from employee as e
inner join employee as m
on e.managerId=m.id
group by e.managerId
having count(e.id)>=5

-- Example 2:
SELECT E1.name
FROM Employee E1
JOIN (
    SELECT managerId, COUNT(*) AS directReports
    FROM Employee
    GROUP BY managerId
    HAVING COUNT(*) >= 5
) E2 ON E1.id = E2.managerId;

-- Example 3:
SELECT m.name
FROM Employee AS e
INNER JOIN Employee AS m ON e.id=m.managerId
GROUP BY m.managerId
HAVING COUNT(m.managerId) >= 5

-- Example 4:
SELECT name
FROM Employee
WHERE id IN (
    SELECT managerId
    FROM Employee
    GROUP BY managerId
    HAVING COUNT(*) >= 5)
