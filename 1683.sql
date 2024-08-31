-- 記得是length，不是python的len

select tweet_id
from tweets
where length(content)>15;
