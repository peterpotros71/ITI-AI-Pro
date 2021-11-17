--1 Write a query to get Product name and quantity/unit 
-- SELECT product_name, quantity_per_unit FROM products;

--2 Write a query to get current Product list (Product ID and name)
-- SELECT product_id, product_name FROM products WHERE discontinued = 0 ORDER BY product_name;

--3 Write a query to get most expense and least expensive Product list (name and unit price)
-- SELECT product_name, unit_price FROM products ORDER BY unit_price DESC LIMIT 1;
-- SELECT product_name, unit_price FROM products ORDER BY unit_price ASC LIMIT 1;
-- SELECT MIN(unit_price) , MAX(unit_price) FROM products;

--4 Write a query to get Product list (id, name, unit price) where current products cost less than $20
-- SELECT product_id, product_name, unit_price FROM products WHERE unit_price < 20 ORDER BY unit_price DESC;

--5 Write a query to get Product list (id, name, unit price) WHERE products cost between $15 and $25.
-- SELECT product_id, product_name, unit_price FROM products WHERE unit_price between 15 and 25 ORDER BY unit_price DESC;

--6 Write a query to get Product list (name, unit price) of above average price
-- SELECT product_id, product_name, unit_price FROM products WHERE unit_price > (SELECT AVG (unit_price) FROM products);

--7 Write a query to get Product list (name, unit price) of ten most expensive products
-- SELECT product_name, unit_price FROM products ORDER BY unit_price DESC LIMIT 10;

--8  Make a list of categories and suppliers who supply products within those categories. 
--SELECT c.product_id, c.product_name, c.supplier_id,  c.category_name , s.contact_name FROM
-- (SELECT * FROM products Inner JOIN categories ON products.category_id = categories.category_id) AS c INNER JOIN suppliers AS s 
-- ON c.supplier_id = s.supplier_id;

--9 Make a complete list of customers, the OrderID and date of any orders they have made. Include customers who have not placed any orders. 
-- SELECT customers.customer_id, orders.order_id, orders.order_date FROM customers LEFT JOIN orders ON customers.customer_id = orders.customer_id;
 
--10 Make a complete list of customers along with the number of orders they have placed. 
--select DISTINCT orders.customer_id, order_id FROM customers INNER JOIN orders ON customers.customer_id = orders.customer_id;

--11 Create a parameterized query that has the user enter a city and then list the customers or suppliers from that city. 
PREPARE get_customers_of_ity(character varying) AS SELECT customer_id, contact_name, city FROM customers WHERE customers.city = $1;
EXECUTE get_customers_of_ity('London');

