-- # SQL 50
-- Customer Who Visited but Did Not Make Any Transactions - LeetCode
-- https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/description/?envType=study-plan-v2&envId=top-sql-50

select
    v.customer_id as customer_id
    , count(v.visit_id) as count_no_trans
from
    Visits v
    left join Transactions t
    on v.visit_id = t.visit_id
where
    t.visit_id is null
group by
    v.customer_id
;
