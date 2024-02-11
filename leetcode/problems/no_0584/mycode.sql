SELECT
    name
FROM
    Customer
WHERE
    not referee_id = 2
    or referee_id is null
;
