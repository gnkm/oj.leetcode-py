-- Replace Employee ID With The Unique Identifier - LeetCode
-- https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/description/?envType=study-plan-v2&envId=top-sql-50

-- my code
-- 3300 ms
SELECT
    unique_id
    , name
FROM
    Employees
    LEFT JOIN EmployeeUNI
    ON Employees.id = EmployeeUNI.id
;

-- Example 1
-- 2000 ms
-- select
-- eu.unique_id as unique_id, e.name as name
-- from Employees e left join EmployeeUNI eu on e.id = eu.id
