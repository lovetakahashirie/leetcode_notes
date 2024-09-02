-- 反正都是做2次select，complxity一樣
select employee_id, department_id
from employee
where primary_flag='Y'
union
select employee_id, department_id
from employee
group by employee_id
having count(employee_id)=1

-- 但是也要熟習用in去解決問題
-- SELECT employee_id, department_id
-- FROM Employee
-- WHERE primary_flag='Y' OR employee_id in
--     (SELECT employee_id
--     FROM Employee
--     Group by employee_id
--     having count(employee_id)=1)
