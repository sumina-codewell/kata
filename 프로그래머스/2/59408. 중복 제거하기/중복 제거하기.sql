-- 코드를 입력하세요
select count(name)
from (
    SELECT name
    from animal_ins
    group by name
) as name_chart