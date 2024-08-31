-- 注意：如果要id!=2，要考慮埋null的情況
-- 像這題，不是2 和 沒填refid的都要算進去

select name
from Customer
where referee_id != 2 or referee_id is null;
