UPDATE index_detail
    JOIN index_info ON index_detail.index_num = index_info.index_num
SET
    index_detail.detail_value = CASE
        WHEN index_info.index_unit = '万元' THEN CASE
            WHEN index_info.index_type = 2 THEN ROUND(RAND() * 900 + 100, 2) * 10
            ELSE ROUND(RAND() * 900 + 100, 2)
        END
        WHEN index_info.index_unit = '亿元' THEN CASE
            WHEN index_info.index_type = 2 THEN ROUND(RAND(), 2) * 10
            ELSE ROUND(RAND(), 2)
        END
        WHEN index_info.index_unit = '亿美元' THEN CASE
            WHEN index_info.index_type = 2 THEN ROUND(RAND(), 2) * 10
            ELSE ROUND(RAND(), 2)
        END
        WHEN index_info.index_unit = '户' THEN CASE
            WHEN index_info.index_type = 2 THEN ROUND(RAND() * 400000 + 100000, 2) * 10
            ELSE ROUND(RAND() * 400000 + 100000, 2)
        END
        WHEN index_info.index_unit = '人' THEN CASE
            WHEN index_info.index_type = 2 THEN ROUND(RAND() * 400000 + 100000, 2) * 10
            ELSE ROUND(RAND() * 400000 + 100000, 2)
        END
        WHEN index_info.index_unit = '笔' THEN CASE
            WHEN index_info.index_type = 2 THEN ROUND(RAND() * 400000 + 100000, 2) * 10
            ELSE ROUND(RAND() * 400000 + 100000, 2)
        END
        WHEN index_info.index_unit = '分' THEN CASE
            WHEN index_info.index_type = 2 THEN ROUND(RAND() * 180 + 20, 2) * 10
            ELSE ROUND(RAND() * 180 + 20, 2)
        END
        WHEN index_info.index_unit = '个' THEN CASE
            WHEN index_info.index_type = 2 THEN ROUND(RAND() * 180 + 20, 2) * 10
            ELSE ROUND(RAND() * 180 + 20, 2)
        END
        WHEN index_info.index_unit = '%' THEN ROUND(RAND() * 100, 2)
        END;