-- 最好畫圖
-- 1. 先將min（change_date）的抽出來，然後這堆人price 10
-- 2. 做一個新table，filter走change_date>date的rows
-- in this case，我只需要抽出change_date<=date的就可以
-- 而1的table是不會顯示的，因爲那些productid全部change_date都>，所以不在這個裏面
-- 剩下的就是group by找max change_date，然後對齊col，最後把price拉出來
-- 最後union在一起就可以


select product_id, 10 as price
from products
group by product_id
having min(change_date)>'2019-08-16'

union

select product_id, new_price as price
from products
where (product_id, change_date)
in 
(select product_id, max(change_date)
from products
where change_date <= '2019-08-16'
group by product_id)



