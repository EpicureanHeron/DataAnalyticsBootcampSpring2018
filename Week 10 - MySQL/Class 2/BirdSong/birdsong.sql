CREATE DATABASE Miscellaneous_DB;

SET SQL_SAFE_UPDATES = 0;

USE Miscellaneous_DB;

SELECT * 
FROM birdsong
WHERE country = 'United Kingdom'
LIMIT 10;

SELECT * 
FROM birdsong
WHERE country = 'United Kingdom'
OR country = 'United States'
LIMIT 20;

SELECT DISTINCT (country)
FROM birdsong;

SELECT species, COUNT(*) as num
FROM birdsong
GROUP BY species
ORDER BY num DESC;

SELECT species
FROM birdsong
WHERE species LIKE 'a%'
LIMIT 10;