SELECT
ANIMAL_ID
,NAME
from ANIMAL_INS
where name like "%el%"
and ANIMAL_TYPE like "dog"
order by name