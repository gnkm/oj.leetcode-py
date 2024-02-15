-- #SQL50
-- Rising Temperature - LeetCode
-- https://leetcode.com/problems/rising-temperature/solutions/3716884/mysql-simple-and-clean-beats-88/?envType=study-plan-v2&envId=top-sql-50

-- id, recordDate, temperature があり、それらは id, 日付, 気温を表す。
-- 日付は連続しているとは限らない。
-- それぞれの日付に対して、その日の温度が前日の温度を超える場合、その日の id を返す。

SELECT
  id
FROM
  Weather
WHERE
  temperature > (
    SELECT
      temperature
    FROM
      Weather t2
    WHERE
      t2.recordDate = DATE_SUB (Weather.recordDate, INTERVAL 1 DAY)
  );

-- 解答例
-- SELECT
--   w1.id
-- FROM
--   Weather w1,
--   Weather w2
-- WHERE
--   DATEDIFF (w1.recordDate, w2.recordDate) = 1
--   AND w1.temperature > w2.temperature;
