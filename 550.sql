-- 記住先把大的，沒有限制的select出來，放到一邊備用
-- 然後再寫下的

select
round(
    count(distinct player_id)/
    (select count(distinct player_id) from activity)
,2) as fraction
from activity
where 
    (player_id, date_add(event_date, interval -1 day))
    in (select player_id, min(event_date) from activity group by player_id);
