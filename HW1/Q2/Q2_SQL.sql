-- [2 points] Create three tables named:

CREATE TABLE SETS (
    set_num TEXT,
    name TEXT,
    year INTEGER,
    theme_id INTEGER,
    num_parts INTEGER
);

CREATE TABLE THEMES (
    id INTEGER,
    name TEXT,
    parent_id INTEGER
);

CREATE TABLE PARTS (
    part_num TEXT,
    name TEXT,
    part_cat_id INTEGER,
    part_material_id INTEGER
);

.mode csv
.import '/data/sets.csv/' SETS
.import '/data/themes.csv/' THEMES
.import '/data/parts.csv/' PARTS

-- BULK INSERT SETS
-- FROM 'sets.csv'
-- WITH
-- (
-- FIRSTROW = 1,
-- FIELDTERMINATOR=',',
-- ROWTERMINATOR='\n',
-- TABLOCK
-- );

-- BULK INSERT THEMES
-- FROM 'themes.csv'
-- WITH
-- (
-- FIRSTROW = 1,
-- FIELDTERMINATOR=',',
-- ROWTERMINATOR='\n',
-- TABLOCK
-- );

-- BULK INSERT PARTS
-- FROM 'parts.csv'
-- WITH
-- (
-- FIRSTROW = 1,
-- FIELDTERMINATOR=',',
-- ROWTERMINATOR='\n',
-- TABLOCK
-- );

CREATE INDEX sets_index ON SETS(set_num);
CREATE INDEX parts_index ON parts(part_num);
CREATE INDEX themes_index ON themes(id);



-- Next question 
CREATE VIEW top_level_themes AS
(SELECT id,name FROM themes WHERE themes.parent_id='');


-- Next question
SELECT count(id) as count FROM top_level_themes;

--Next question

SELECT name,count from 
(
SELECT name,count(id) as count FROM top_level_themes
order BY
count  DESC
);


-- Next question

select theme, 


theme,percentage

Space,10.30

Town,7.33

Castle,5.00




 CREATE VIEW top_level_themes
 AS SELECT id,name FROM themes where parent_id  = ‘’;



CREATE TABLE SETS (
    set_num TEXT,
    name TEXT,
    year INTEGER,
    theme_id INTEGER,
    num_parts INTEGER
);
CREATE TABLE THEMES (
    id INTEGER,
    name TEXT,
    parent_id INTEGER
);
CREATE TABLE PARTS (
    part_num TEXT,
    name TEXT,
    part_cat_id INTEGER,
    part_material_id INTEGER



(CREATE UNIQUE INDEX RowID on sets_years(1)),

CREATE VIEW sets_years
AS select set_nmu,year,count(set_num)
from
SETS
group by year;



REATE VIEW top_level_themes
 AS SELECT id,name FROM themes where parent_id  = ‘’;





select T1.name,count(T2.set_num)/(select count(theme_id) from SETS) as set_count_percent
from top_level_themes as T1
join 
SETS as T2
ON
T1.id=T2.theme_id
group by T1.NAME
order by set_count_percent DESC
limit 10;

select T1.name,printf("%.2f",(count(T2.set_num)/(select count(theme_id) from SETS))*100) as set_count_percent
from top_level_themes as T1
join 
SETS as T2
ON
T1.id=T2.theme_id
group by T1.NAME
order by set_count_percent ASC
limit 10;

-- with data as (
--   select
--     date_trunc('day', created_at) as day,
--     count(1)
--   from users
--   group by 1
-- )

-- select
--   day,
--   sum(count) over (order by day asc rows between unbounded preceding and current row)
-- from data




CREATE VIEW sets_years
AS select set_num,year,count(set_num) as count_sum_num
from
SETS
group by year;


select year,sum(count_sum_num) over(PARTITION by year order by year) as cumulative_sum
from sets_years
order by year;


















