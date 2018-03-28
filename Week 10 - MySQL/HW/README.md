-- Switch to sakila DB

`USE sakila;`

-- Display First and Last Name of all actors

```SELECT first_name, last_name
FROM actor;```

-- Display first and last name of all actors in a single column named 'Actor Name'in all caps

```SELECT CONCAT(UPPER(first_name), ' ', UPPER(last_name))
AS 'Actor Name'
FROM actor; -- already in all caps?```

-- get the ID number, first name, and last name of an actor, with the first name "Joe."

`SELECT actor_id, first_name, last_name
FROM actor
WHERE actor.first_name LIKE 'Joe';`

-- Find all actors whose last name contain the letters GEN

`SELECT actor_id, first_name, last_name
FROM actor
WHERE actor.last_name LIKE '%GEN%';`

-- Find all actors whose last names contain the letters LI and order the rows by last name and first name, in that order:

`SELECT actor_id, first_name, last_name
FROM actor
WHERE actor.last_name LIKE '%LI%'
ORDER BY last_name, first_name;`

-- Using IN, display the country_id and country columns of the following countries: Afghanistan, Bangladesh, and China:

`SELECT country_id, country
FROM country
WHERE country.country IN ('Afghanistan', 'Bangladesh', 'China');`

-- Add a middle_name column to the table actor.
-- Position it between first_name and last_name.

`ALTER TABLE actor
ADD COLUMN middle_Name VARCHAR(10) NULL
AFTER first_name;`

-- change middle name type to BLOB

`ALTER TABLE actor
MODIFY middle_name BLOB;`

-- delete middle name column

`ALTER TABLE actor
DROP COLUMN middle_name;`

-- List the last names of actors, as well as how many actors have that last name

`SELECT last_name, COUNT(last_name)
FROM actor
GROUP BY last_name;`

-- List last names of actors and the number of actors who have that last name
-- but only for names that are shared by at least two actors

`SELECT last_name, COUNT(last_name) as Num
FROM actor
GROUP BY last_name
HAVING Num >= 2;`

-- replace GROUCHO WILLIAMS with HARPO WILLIAMS

`UPDATE actor
SET first_name = 'HARPO'
WHERE actor.first_name = 'GROUCHO'
AND actor.last_name = 'WILLIAMS';`

-- if the first name of the actor is currently HARPO, change it to GROUCHO.
-- Otherwise, change the first name to MUCHO GROUCHO
--  using a unique identifier update the record

`UPDATE actor
SET first_name= CASE
   WHEN first_name='HARPO' THEN 'GROUCHO'
   ELSE 'MUCHO GROUCHO'
END
WHERE actor_id = 172;`

-- show query to recreate address table

`SHOW CREATE TABLE address;`

-- Use JOIN to display the first and last names, as well as the address, of each staff member.
-- Use the tables staff and address:

`SELECT staff.first_name, staff.last_name, address.address
FROM staff
LEFT JOIN address ON staff.address_id = address.address_id;`

-- Use JOIN to display the total amount rung up by each staff member in August of 2005.

`SELECT staff.first_name, staff.last_name, SUM(payment.amount) as Total
FROM payment
LEFT JOIN staff ON staff.staff_id = payment.staff_id
WHERE payment.payment_date LIKE '2005-08%'
GROUP BY staff.last_name, staff.first_name;`

-- List each film and the number of actors who are listed for that film. Use tables film_actor and film. Use inner join.

`SELECT film.title, COUNT(film_actor.actor_id) as num_of_actors
FROM film_actor
INNER JOIN film ON film_actor.film_id = film.film_id
GROUP BY film.title;`

-- get the # of copies of the film Hunchback Impossible in the inventory system

`SELECT count(inventory.film_id)
FROM inventory
WHERE inventory.film_id = (SELECT film_id
												FROM film
												WHERE film.title = 'Hunchback Impossible');`

--  list the total paid by each customer & List the customers alphabetically by last name

`SELECT customer.first_name, customer.last_name, SUM(payment.amount) as Total
FROM payment
LEFT JOIN customer ON customer.customer_id = payment.customer_id
GROUP BY customer.first_name, customer.last_name
ORDER BY customer.last_name ASC;`

-- display the titles of movies starting with the letters K and Q whose language is English

`SELECT film.title
FROM film
WHERE film.language_id = (SELECT language_id
												FROM language
                                                WHERE language.name = 'English')
AND film.title LIKE 'K%'
OR film.title LIKE 'Q%';`

-- Use subqueries to display all actors who appear in the film Alone Trip.

`SELECT actor.first_name, actor.last_name
FROM actor
WHERE actor.actor_id = ANY (SELECT actor_id
													FROM film_actor
													WHERE film_actor.film_id = (SELECT film_id
																									FROM film
																									WHERE film.title = 'Alone Trip')
													);`

-- get the names and email addresses of all Canadian customers

`SELECT customer.first_name, customer.last_name, customer.email
FROM customer
INNER JOIN address
	ON address.address_id = customer.address_id
INNER JOIN city
	ON address.city_id = city.city_id
INNER JOIN country
	ON city.country_id = country.country_id
WHERE country.country = 'Canada';`

-- Identify all movies categorized as famiy films

`SELECT title
FROM film
WHERE film.film_id = ANY (SELECT film_id
												FROM film_category
												WHERE film_category.category_id = (SELECT category_id
																												FROM category
																												WHERE name = 'Family')
											);`

-- Display the most frequently rented movies in descending order

`SELECT title, COUNT(rental.inventory_id) as Times_Rented
FROM film
INNER JOIN inventory
	ON film.film_id = inventory.film_id
INNER JOIN rental
	ON inventory.inventory_id = rental.inventory_id
GROUP BY film.title
ORDER BY Times_Rented DESC;`

-- display how much business, in dollars, each store brought in

`SELECT store.store_id, SUM(payment.amount) as Revenue
FROM store
INNER JOIN staff
	ON store.store_id = staff.store_id
INNER JOIN payment
	ON payment.staff_id = staff.staff_id
GROUP BY store.store_id
ORDER BY Revenue DESC;`

-- display for each store its store ID, city, and country

`SELECT store.store_id, city.city, country.country
FROM store
INNER JOIN address
	ON store.address_id = address.address_id
INNER JOIN city
	ON address.city_id = city.city_id
INNER JOIN country
	ON city.country_id = country.country_id;`

-- List the top five genres in gross revenue in descending order

`SELECT
    category.name AS Genre, SUM(payment.amount) AS Revenue
FROM
    category
        INNER JOIN
    film_category ON category.category_id = film_category.category_id
        INNER JOIN
    inventory ON film_category.film_id = inventory.film_id
        INNER JOIN
    rental ON inventory.inventory_id = rental.inventory_id
        INNER JOIN
    payment ON rental.rental_id = payment.rental_id
GROUP BY category.name
ORDER BY Revenue DESC
LIMIT 5;`

-- create a view

```CREATE VIEW `sakila`.`top_5_categories` AS
    SELECT
        `sakila`.`category`.`name` AS `Genre`,
        SUM(`sakila`.`payment`.`amount`) AS `Revenue`
    FROM
        ((((`sakila`.`category`
        JOIN `sakila`.`film_category` ON ((`sakila`.`category`.`category_id` = `sakila`.`film_category`.`category_id`)))
        JOIN `sakila`.`inventory` ON ((`sakila`.`film_category`.`film_id` = `sakila`.`inventory`.`film_id`)))
        JOIN `sakila`.`rental` ON ((`sakila`.`inventory`.`inventory_id` = `sakila`.`rental`.`inventory_id`)))
        JOIN `sakila`.`payment` ON ((`sakila`.`rental`.`rental_id` = `sakila`.`payment`.`rental_id`)))
    GROUP BY `sakila`.`category`.`name`
    ORDER BY `Revenue` DESC
    LIMIT 5;```

-- delete that view

`DROP VIEW top_5_categories;`
