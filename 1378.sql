-- 首先要搞清楚題目要哪個col全顯示，就是all names都要顯示
-- 我就要將有name col的table set成左，再left join其他table
-- 那就自然會顯示all name，有些name unique id 的就null

select EmployeeUNI.unique_id, Employees.name
from Employees left join Employeeuni
on EmployeeUNI.id = Employees.id;
