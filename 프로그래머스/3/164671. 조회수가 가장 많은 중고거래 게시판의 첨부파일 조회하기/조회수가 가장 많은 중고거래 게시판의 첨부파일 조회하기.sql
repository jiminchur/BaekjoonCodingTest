SELECT
concat("/home/grep/src/",f.BOARD_ID,"/",f.FILE_ID,f.FILE_NAME,f.FILE_EXT) 
as FILE_PATH
from USED_GOODS_FILE f
join USED_GOODS_BOARD b on f.BOARD_ID = b.BOARD_ID
where b.views = (select max(views) from USED_GOODS_BOARD)
order by f.file_id desc