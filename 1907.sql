-- sum(if(,,))好像不太行，像是syntax問題
-- 其實就是把3種的拼在一起，想想其實跟excel差不多，自己寫個row name，然後算一次sum if

select
    'Low Salary' as category,
    sum(income<20000) as accounts_count
from accounts
union
select
    'Average Salary' as category,
    sum(income>=20000 and income<=50000) as accounts_count
from accounts
union
select
    'High Salary' as category,
    sum(income>50000) as accounts_count
from accounts
