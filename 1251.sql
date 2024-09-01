-- 要考慮全部product，因爲他可能沒sell 過就不會出現在inner join
-- 再用ifnull變成0出現在最終結果
-- 記得用group by 分區計算
select p.product_id, ifnull(round(sum(p.price*u.units)/sum(u.units),2),0) as average_price
from prices p left join unitssold u
on p.product_id = u.product_id
and u.purchase_date between p.start_date and p.end_date
group by p.product_id;
