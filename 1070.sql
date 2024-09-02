-- 要一個col找min/max之類的，而又要另一個col的values是corresponding row是不能一次做完的，因爲會移位。唯一的解法是先把min(year)抽出來，再用in去match對應的整個col，這樣就有min(year),其他col在同一個row

select product_id, year as first_year, quantity, price
from sales
where (product_id, year)
in (select product_id, min(year) from sales group by product_id);
