-- 你已經學會了group by，但要用好having，就是group by 后的where
select customer_id
from customer
group by customer_id
having (select count(distinct product_key) from product)=count(distinct product_key)
