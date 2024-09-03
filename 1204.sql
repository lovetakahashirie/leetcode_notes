
-- select q1.person_name
-- from queue q1 left join queue q2
-- on q1.turn>=q2.turn
-- group by q1.turn
-- having sum(q2.weight)<=1000
-- order by sum(q2.weight) desc
-- limit 1

-- 先用over function+order by計算cumulative weight
-- 剩下就是where filter走後面的
-- order by desc反過來
-- limit抽出第一個
select t.person_name
from 
(select *, sum(weight) over (order by turn asc) as cum from queue) t
where t.cum <= 1000
order by t.turn desc
limit 1





