-- 遇到什麽xxx rate之類的，直接用avg，再跟個0/1，就省區計算%的問題
-- 記得加上group by，一個一個區間去計算

select s.user_id, round(avg(if(c.action='confirmed',1,0)),2) as confirmation_rate
from signups s left join confirmations c
on s.user_id = c.user_id
group by s.user_id;

