-- 注意執行順序，select 那行改名了，所以order by身爲selec之後執行的，就要用id名，而不是author_id

select distinct author_id as id
from views
where author_id = viewer_id
order by id asc;
