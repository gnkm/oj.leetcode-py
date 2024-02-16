-- #SQL50
-- Students and Examinations - LeetCode
-- https://leetcode.com/problems/students-and-examinations/?envType=study-plan-v2&envId=top-sql-50

-- Example 1:
SELECT
  s.student_id
  , s.student_name
  , sub.subject_name
  , COUNT(e.student_id) AS attended_exams
FROM
  Students s
  CROSS JOIN Subjects sub
  LEFT JOIN Examinations e ON s.student_id = e.student_id AND sub.subject_name = e.subject_name
GROUP BY
  s.student_id
  , s.student_name
  , sub.subject_name
ORDER BY
  s.student_id
  , sub.subject_name;
;

-- copilot
-- Write a solution to find the number of times each student attended each exam.
-- Return the result table ordered by student_id and subject_name.

-- select
--   Students.student_id as student_id
--   , Students.student_name as student_name
--   , Examinations.subject_name as subject_name
--   , count(Examinations.subject_name) as attended_exams
-- from
--     Students
--     right join Examinations on Students.student_id = Examinations.student_id
-- group by
--     Students.student_id
--     , Examinations.subject_name
-- order by
--     Students.student_id
--     , Students.subject_name
-- ;
