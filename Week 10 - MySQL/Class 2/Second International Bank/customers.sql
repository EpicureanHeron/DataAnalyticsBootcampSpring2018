CREATE DATABASE Second_International_Bank;

USE Second_International_Bank;

create table Customers(
  id INTEGER AUTO_INCREMENT NOT NULL, PRIMARY KEY(id) ,
	FirstName VARCHAR(30) NOT NULL,
	LastName VARCHAR(30) NOT NULL,
	Loan BOOLEAN NOT NULL,
    Checking DECIMAL(10,2) NOT NULL,
    Savings DECIMAL(10,2) NOT NULL);


INSERT INTO Customers(FirstName, LastName, Loan, Checking, Savings)
	VALUES('Billy', 'Armstrong', TRUE, 100000.34, 50000.92),
    ('Antonio', 'Brown', FALSE, 1000000.82, 2003403.51),
    ('Sidney', 'Crosby', TRUE, 300000.24, 10000.22),
    ('Joey', 'Porter', FALSE, 500000.19, 83.11),
    ('Mike', 'Artman', FALSE, 234021.88, 2344.92)
