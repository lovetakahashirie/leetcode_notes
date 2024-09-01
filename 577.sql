-- 注意null也要算進去，因爲null不能被計算就沒被考慮進去
-- 主要不是=，是is

select e.name, b.bonus
from Employee e left join bonus b
on e.empid = b.empid
where b.bonus<1000 or b.bonus is null;
