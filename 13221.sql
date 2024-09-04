-- 要distinct，因爲同一天可以有>1來消費，但是我只需要顯示這7天的amt一次（same date, sum amount一樣的）。爲了避免這種情況，我直接distinct，那就remove了duplicate
-- 要善用over，我要先order by date，再只要7天的window range，然後計算
-- sum/7，不能直接avg of 7days，因爲每天可以>1 row，如果avg了，就可能/>7
-- offset是跳過頭n個，前面一定要有limit

select distinct
    visited_on,
    sum(amount) over (order by visited_on asc range between interval 6 day preceding and current row) as amount,
    round(sum(amount) over (order by visited_on asc range between interval 6 day preceding and current row)/7,2)as average_amount
from customer
limit 9999999
offset 6
