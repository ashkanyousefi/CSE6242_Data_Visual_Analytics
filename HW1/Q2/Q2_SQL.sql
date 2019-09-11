-- [2 points] Create three tables named:

CREATE TABLE SETS (
    set_num TEXT,
    name TEXT,
    year INTEGER,
    theme_id INTEGER,
    num_parts INTEGER,
);

CREATE TABLE THEMES (
    id INTEGER,
    name TEXT,
    parent_id INTEGER,
);

CREATE TABLE PARTS (
    part_num TEXT,
    name TEXT,
    part_cat_id INTEGER,
    part_material_id INTEGER,
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
count  DEC
);


-- Next question



















