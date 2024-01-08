-- 코드를 입력하세요
SELECT
a.APNT_NO
,p.PT_NAME
,a.PT_NO
,a.MCDP_CD
,d.DR_NAME
,a.APNT_YMD
from APPOINTMENT a
join PATIENT p on a.PT_NO=p.PT_NO
join DOCTOR d on d.DR_ID=a.MDDR_ID
where a.APNT_YMD like "2022-04-13%"
and a.MCDP_CD like "CS"
and a.APNT_CNCL_YN like "N"
order by a.APNT_YMD asc