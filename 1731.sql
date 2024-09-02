-- consider a manager an employee who has at least 1 other employee reporting to them，我就self join
-- 只抽出我想看的col出來看看
-- count, avg，both group by，所以不用subquery...in
-- 最後就order by
select e2.employee_id, e2.name, count(*) as reports_count, round(avg(e1.age),0) as average_age
from employees e1, employees e2
where e1.reports_to = e2.employee_id
group by e1.reports_to
order by e2.employee_id
