-- 注意（）開關
-- 先把要的min抽出來一個table，然後再接它
-- 剩下的就計算

select round(avg(order_date=customer_pref_delivery_date)*100,2) as immediate_percentage
from delivery
where (customer_id, order_date) in 
(select customer_id, min(order_date)
from delivery
group by customer_id);
