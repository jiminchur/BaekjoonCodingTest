-- 코드를 입력하세요
SELECT
p.CART_ID
from CART_PRODUCTS p
join (select CART_ID from CART_PRODUCTS where NAME = "Yogurt") q on p.CART_ID=q.CART_ID
where p.NAME like "Milk"


