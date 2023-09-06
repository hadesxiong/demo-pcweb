-- SELECT index_num,detail_belong,detail_date,detail_value as result
-- FROM index_detail
-- WHERE (detail_date = '2023-01-31' AND 
-- index_num IN (SELECT index_num from index_info where index_class=1) AND
-- detail_belong in (SELECT org_num FROM org_info WHERE org_group=3))
-- GROUP BY index_num, detail_date, detail_belong, detail_value
-- ORDER BY index_num, detail_value DESC

-- SET @row_number := 0, @prev_index_num := NULL;
-- SELECT t.index_num, t.detail_belong, t.detail_date, t.detail_value AS result
-- FROM (
--     SELECT 
--         index_num, 
--         detail_belong, 
--         detail_date, 
--         detail_value,
--         CASE
--             WHEN @prev_index_num = index_num THEN @row_number := @row_number + 1
--             ELSE @row_number := 1
--         END AS row_number,
--         @prev_index_num := index_num
--     FROM index_detail
--     CROSS JOIN (SELECT @row_number := 0, @prev_index_num := NULL) AS vars
--     WHERE (detail_date = '2023-01-31' 
--            AND index_num IN (SELECT index_num FROM index_info WHERE index_class in (1,2,3,4,5)) 
--            AND detail_belong IN (SELECT org_num FROM org_info WHERE org_group in (3)))
--     ORDER BY index_num, detail_value DESC
-- ) AS t
-- WHERE t.row_number <= 5
-- ORDER BY t.index_num, t.detail_value DESC;

SET @row_number := 0, @prev_index_num := NULL;
SELECT t.index_num, t.detail_belong, t.detail_date, t.detail_value AS result,
       (SELECT detail_value
        FROM index_detail AS d
        WHERE d.index_num = t.index_num
          AND d.detail_belong = t.detail_belong
          AND d.detail_date = '2023-01-01'  -- 用您的特定日期替换此处
          AND d.detail_type = 1  -- 匹配特定的detail_type
        ORDER BY d.detail_value DESC
        LIMIT 1) AS matching_detail_value
FROM (
    SELECT 
        index_num, 
        detail_belong, 
        detail_date, 
        detail_value,
        CASE
            WHEN @prev_index_num = index_num THEN @row_number := @row_number + 1
            ELSE @row_number := 1
        END AS row_number,
        @prev_index_num := index_num
    FROM index_detail
    CROSS JOIN (SELECT @row_number := 0, @prev_index_num := NULL) AS vars
    WHERE (detail_date = '2023-01-31' 
           AND index_num IN (SELECT index_num FROM index_info WHERE index_class in (1,2,3,4,5)) 
           AND detail_belong IN (SELECT org_num FROM org_info WHERE org_group in (3)))
    ORDER BY index_num, detail_value DESC
) AS t
WHERE t.row_number <= 5
ORDER BY t.index_num, t.detail_value DESC;