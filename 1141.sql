-- 要清楚題目，寫下所有要求，然後一個一個去check

select activity_date as day, count(distinct user_id) as active_users
from activity
where activity_type is not null
and activity_date between date_add('2019-07-27', interval -29 day)and '2019-07-27'
group by activity_date;
