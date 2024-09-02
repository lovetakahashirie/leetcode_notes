-- 考驗你，當where 不能用count/aggregate function時
-- 要用having去解決

select class
from courses
group by class
having count(student)>=5;
