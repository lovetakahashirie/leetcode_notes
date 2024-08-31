-- left join是因爲有些customer沒有transact，但我要連過去再remove走no transact的
-- where t.transat is null而不是t.amt，因爲amt可以是null的transact，transact is null就代表根本沒有這個交易（最好跟題目，without transaction）

select v.customer_id, count(v.visit_id) as count_no_trans 
from visits v left join Transactions t
on v.visit_id = t.visit_id
where t.transaction_id is null
group by v.customer_id;
