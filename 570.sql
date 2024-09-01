-- 今次就對了，先拆開來看，然後再看
select name
from
(select e2.id, e2.name, count(e2.id) as count
from Employee e1
left join Employee e2
on e1.managerId = e2.id
group by e2.id) as t
where count>=5;
