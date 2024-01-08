-- 코드를 입력하세요
SELECT
b.AUTHOR_ID
,a.AUTHOR_NAME
,b.CATEGORY
,sum(s.SALES*b.PRICE) as TOTAL_SALES
from book b
join AUTHOR a on b.AUTHOR_ID=a.AUTHOR_ID
join BOOK_SALES s on b.BOOK_ID=s.BOOK_ID
where s.SALES_DATE like "2022-01%"
group by 1,3
order by b.AUTHOR_ID, b.CATEGORY desc