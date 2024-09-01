-- 要在裏面先算好total # users，然後算分區出席人數

select r.contest_id, round((count(r.user_id)/(select count(1) from users))*100,2) as percentage
from register r left join users u
on r.user_id = u.user_id
group by r.contest_id
order by percentage desc, contest_id asc;


-- select count(1) from users;
