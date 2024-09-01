-- 先將cross出來，確保全部都在，然後對齊
-- 下一步是算avg exp years，用group by分區計算

select p.project_id, round(avg(e.experience_years),2) as average_years
from project p cross join employee e on p.employee_id=e.employee_id
group by p.project_id;
