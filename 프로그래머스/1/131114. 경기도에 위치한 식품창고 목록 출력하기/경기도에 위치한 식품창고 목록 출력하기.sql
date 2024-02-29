-- 코드를 입력하세요
SELECT warehouse_id, warehouse_name, address, coalesce(freezer_yn, 'N')
from food_warehouse
WHERE ADDRESS LIKE'%경기%'
order by warehouse_id