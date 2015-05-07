SELECT FirstName, LastName, Title FROM employees;
SELECT FirstName FROM employees WHERE City = "Seattle";
SELECT FirstName FROM employees WHERE City = "London";
SELECT FirstName FROM employees WHERE Title LIKE "%Sales%";
SELECT FirstName FROM employees WHERE Title LIKE '%Sales%'
AND (TitleOfCourtesy = 'Mrs.' OR TitleOfCourtesy = 'Ms.');

SELECT FirstName FROM employees  ORDER BY BIrthDate LIMIT 5;
SELECT FirstName FROM employees ORDER BY HireDate LIMIT 5;
SELECT FirstName FROM employees WHERE ReportsTo IS NULL;

SELECT A.FirstName, A.LastName, B.FirstName, B.LastName FROM employees AS A
JOIN employees AS B ON A.ReportsTo = B.EmployeeID;

SELECT COUNT (*) FROM employees WHERE (TitleOfCourtesy = 'Mrs.' OR TitleOfCourtesy = 'Ms.');
SELECT COUNT (*) FROM employees WHERE (TitleOfCourtesy = 'Mr.' OR TitleOfCourtesy = 'Dr.');

SELECT COUNT(*) FROM employees GROUP BY City;

SELECT OrderID, FirstName, LastName FROM orders
JOIN employees ON orders.EmployeeID = employees.EmployeeID;

SELECT OrderID, CompanyName FROM orders
JOIN shippers ON orders.ShipVia = shippers.ShipperID;

SELECT COUNT(*) FROM orders GROUP BY ShipCountry;

SELECT FirstName, LastName FROM employees AS A
INNER JOIN orders AS B ON A.EmployeeID = B.EmployeeID
GROUP BY B.EmployeeID
ORDER BY COUNT(OrderID) DESC LIMIT 1;

SELECT A.OrderID, B.FirstName, B.LastName, C.CompanyName
FROM orders AS A
JOIN employees AS B ON A.EmployeeID = B.EmployeeID
JOIN customers AS C ON A.CustomerID = C.CustomerID;

SELECT a.OrderID, b.CompanyName, c.CompanyName
FROM orders AS A
JOIN customers AS B ON A.CustomerID = B.CustomerID
JOIN shippers AS C ON A.ShipVia = C.ShipperID;