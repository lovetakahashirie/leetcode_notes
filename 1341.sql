-- 好好把要求寫下來，再一步一步寫出來就可以
-- order by 可以用aggre，那就不用先count再max寫兩次
-- union之間要()
-- 要union all，因爲會同名，就吃掉了

(select u.name as results
from movierating mr join users u
on mr.user_id = u.user_id
group by mr.user_id
order by count(*) desc, u.name asc
limit 1)

union all

(select m.title
from movies m join movierating mr
on m.movie_id = mr.movie_id
where month(mr.created_at) = 2
and year(mr.created_at) = 2020
group by mr.movie_id
order by avg(mr.rating) desc, m.title asc
limit 1)

