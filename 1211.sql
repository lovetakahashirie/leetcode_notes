-- 基本上沒問題了，可以試試向著excel function的思路去寫

select
    query_name,
    round(avg(rating/position),2) as quality,
    round(sum(if(rating<3,1,0))/count(1)*100,2) as poor_query_percentage
from queries
where query_name is not null
group by query_name;


