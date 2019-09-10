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
.import '//data/sets.csv/' SETS
.import '//data/themes.csv/' THEMES
.import '//data/parts.csv/' PARTS

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



