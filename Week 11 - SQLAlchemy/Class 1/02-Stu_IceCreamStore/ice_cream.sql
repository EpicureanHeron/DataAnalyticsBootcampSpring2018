USE Miscellaneous_DB;

CREATE TABLE ice_cream(
	id INTEGER AUTO_INCREMENT NOT NULL, PRIMARY KEY(id) ,
	flavor VARCHAR(50) NOT NULL,
	rating INTEGER(4) NOT NULL,
	price FLOAT(10) NOT NULL);
    
INSERT INTO ice_cream(flavor, rating, price)
VALUES('Cookie Dough', 100, 2.95),
	('Vanilla', 60, 1.25),
	('Rocky Road', 90, 3.05),
	('Chocolate', 75, 1.25),
	('Turtle', 100, 3.00);
    
SELECT * FROM ice_cream;

SELECT * FROM ice_cream
WHERE ice_cream.price = 1.25