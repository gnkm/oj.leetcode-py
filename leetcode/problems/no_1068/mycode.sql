-- #SQL50
-- Product Sales Analysis I - LeetCode
-- https://leetcode.com/problems/product-sales-analysis-i/description/?envType=study-plan-v2&envId=top-sql-50

select
    p.product_name as product_name
    , s.year as year
    , s.price as price
from
    Sales s
    left join Product p on s.product_id = p.product_id
;

-- 模範解答
-- SELECT
--     DISTINCT p.product_name, s.year, s.price
-- FROM
--     Sales s
-- JOIN
--     Product p
-- ON
--     s.product_id = p.product_id
