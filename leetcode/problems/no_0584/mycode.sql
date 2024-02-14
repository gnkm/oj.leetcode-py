-- # SQL 50
-- Find Customer Referee - LeetCode
-- https://leetcode.com/problems/find-customer-referee/description/?envType=study-plan-v2&envId=top-sql-50

SELECT
    name
FROM
    Customer
WHERE
    not referee_id = 2
    or referee_id is null
;
