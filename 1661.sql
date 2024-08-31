-- 沒太多說的，先把要的東西拿出來，一點一點去run query慢慢拆小那個table
-- 另外記得group by的用法，是在count時告訴他我要count這些分區每個區的count

select a1.machine_id, round(sum(a2.timestamp-a1.timestamp)/count(a1.process_id), 3) as processing_time
from Activity a1, Activity a2
where a1.process_id = a2.process_id and a1.machine_id = a2.machine_id and a1.activity_type = 'start' and a2.activity_type = 'end'
group by a1.machine_id;
