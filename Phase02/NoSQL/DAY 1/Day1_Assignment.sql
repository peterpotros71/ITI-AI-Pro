USE Books;

--1) Display Title ID , price , sales  and revenue for each book (Title)in the books DB, Display titles by descending revenue
--UPDATE dbo.titles SET (price * sales) AS revenue;
--ALTER TABLE dbo.titles ADD  revenue int;
--UPDATE dbo.titles SET revenue = price * sales;
SELECT title_id, price, sales, (price * sales) AS revenue FROM dbo.titles ORDER BY revenue DESC;


--2) Display titles that generated more than $1 million in revenue
SELECT title_name, (price * sales) AS revenue FROM dbo.titles WHERE (price * sales) > 1000000;


--3) Display the authors who live in New York State, Colorado, or San Francisco.
SELECT au_fname, au_lname, city, state FROM dbo.authors WHERE state IN ('NY', 'CO', 'CA') AND city IS NOT NULL;

--4) display the authors who live outside the 212,415, and 303 area codes
SELECT au_fname, au_lname, phone FROM dbo.authors WHERE phone NOT LIKE '212%' AND phone NOT LIKE '415%' AND phone NOT LIKE '303%';


--5) display the titles published in 2000
SELECT title_id, pubdate FROM dbo.titles WHERE YEAR(pubdate) = 2000;


--6) display the titles published on the first day of the year 2000, 2001, or 2002
SELECT title_id, pubdate FROM dbo.titles WHERE YEAR(pubdate) IN (2000,2001,2002) AND Month(pubdate) = 01 AND DAY(pubdate) = 01;


--7) Display the biographies whose (past or future) publication dates are known
SELECT title_id, type, pubdate FROM dbo.titles WHERE type = 'biography' AND pubdate IS NOT NULL;


--8) display the book old prices and discounte them by 10 percent, display prices after discount (new price)
SELECT title_id, price, ('0.10') AS Disacount, (price - .1 * price) AS New_Price FROM dbo.titles


--9) display biographies by descending publication date.
SELECT title_id, pubdate FROM dbo.titles WHERE type = 'biography' AND pubdate IS NOT NULL ORDER BY pubdate DESC; 


--10) Display all the authors named Klee Hull.
SELECT au_id , au_fname, au_lname FROM dbo.authors WHERE au_fname = 'Klee' AND au_lname = 'Hull';


--11) Display  the first initial and last name of the authors from New York State and Colorado
SELECT SUBSTRING(au_fname, 1, 1) + '. ' + au_lname AS AutherName FROM dbo.authors WHERE state IN ('NY', 'CO');
