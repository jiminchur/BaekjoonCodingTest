SELECT
i.ANIMAL_ID
,i.ANIMAL_TYPE
,i.NAME
from ANIMAL_INS i
join ANIMAL_OUTS o on o.ANIMAL_ID=i.ANIMAL_ID
where 1=1
and i.SEX_UPON_INTAKE like "Intact%"
and (o.SEX_UPON_OUTCOME like "Spayed%" or o.SEX_UPON_OUTCOME like "Neutered%")
order by i.ANIMAL_ID