-- 코드를 입력하세요
SELECT
YEAR(o.SALES_DATE) as YEAR,
MONTH(o.SALES_DATE) as MONTH,
u.GENDER,
count(distinct(u.USER_ID)) as USERS
from ONLINE_SALE o
join USER_INFO u on u.USER_ID=o.USER_ID
where u.GENDER is not null
group by 1,2,3
order by 1,2,3



