-- 這個不能用，因爲limit后，不能出null
-- select ifnull(num,null) as num
-- from mynumbers
-- group by num
-- having count(num)=1
-- order by num desc
-- limit 1

-- 要先把nums抽出來（記得ifnull），然後在max，如果沒有max就會自動null
select max(num) as num
from
(select ifnull(num,null) as num
from mynumbers
group by num
having count(num)=1) as subq;
