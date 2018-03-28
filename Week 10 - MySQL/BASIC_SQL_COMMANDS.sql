-- create db
CREATE DATABASE animals_db

-- move to use specified db
USE animals_db

-- create a table
create table people(
  id INTEGER AUTO_INCREMENT NOT NULL, PRIMARY KEY(id) ,
	name VARCHAR(30) NOT NULL,
	has_pet BOOLEAN NOT NULL,
	pet_name VARCHAR(30),
	pet_age INTEGER(3));

-- insert data
INSERT INTO people(name, has_pet, pet_name, pet_age)
	VALUES('Dylan', TRUE, 'Shoei', 8)

-- select all data from the people table where people have a pet
SELECT * FROM people WHERE has_pet = TRUE;

-- update a row
UPDATE people
SET has_pet = FALSE
WHERE (name = 'Dylan')
