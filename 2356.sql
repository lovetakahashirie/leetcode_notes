-- 經典的，看清楚題目
-- +清楚知道你要什麽分區，基本上就會了
select teacher_id, count(distinct subject_id) as cnt
from teacher
group by teacher_id;
