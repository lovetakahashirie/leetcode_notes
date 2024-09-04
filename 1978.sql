-- 沉住氣，一步一步去拆解，從m_id left開始找，一直坐上去

select employee_id
from employees
where salary < 30000
and manager_id in
(select manager_id
from employees
where manager_id not in (select employee_id from employees))
order by employee_id
