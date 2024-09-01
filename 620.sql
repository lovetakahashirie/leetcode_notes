-- 想好int 找odd就是mod =1

select *
from cinema
where id%2=1 and description != 'boring'
order by rating desc;
