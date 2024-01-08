SELECT date_format(SALES_DATE,"%Y-%m-%d"), PRODUCT_ID, USER_ID, SALES_AMOUNT
FROM (
    SELECT SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT, '온라인' AS SALE_TYPE
    FROM ONLINE_SALE
    WHERE SALES_DATE BETWEEN '2022-03-01' AND '2022-03-31'
    UNION ALL
    SELECT SALES_DATE, PRODUCT_ID, NULL AS USER_ID, SALES_AMOUNT, '오프라인' AS SALE_TYPE
    FROM OFFLINE_SALE
    WHERE SALES_DATE BETWEEN '2022-03-01' AND '2022-03-31'
) COMBINED_SALES
ORDER BY SALES_DATE ASC, PRODUCT_ID ASC, COALESCE(USER_ID, 0) ASC;
