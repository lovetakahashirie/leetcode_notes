-- 有個叫alias reference的東西，雖然group by 比起select更早執行，但是可以ref 在select時create的column
-- 當成excel create new columns就可以

select
    DATE_FORMAT(trans_date, '%Y-%m') as month,
    country,
    count(state) as trans_count,
    sum(if(state='approved',1,0)) as approved_count,
    sum(amount) as trans_total_amount,
    sum(if(state='approved',amount,0)) as approved_total_amount
from Transactions
group by month, country;
