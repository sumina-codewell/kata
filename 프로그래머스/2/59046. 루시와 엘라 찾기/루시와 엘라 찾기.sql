-- 코드를 입력하세요
SELECT animal_id, name, sex_upon_intake
from animal_ins
where name in ('Lucy','Rogan','Sabrina','Ella','Pickle','Mitty')
order by animal_id