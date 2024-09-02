-- 最經典的，考你group by
-- 總之記住group by就是分區計算 

select user_id, count(follower_id) as followers_count
from followers
group by user_id
order by user_id asc
