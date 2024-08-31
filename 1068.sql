-- 要看清楚是left join還是單純inner join
-- 他説要for each sales_id，代表全部sales_id都要考慮進去


select p.product_name, s.year, s.price
from sales s left join product p
on s.product_id = p.product_id;
