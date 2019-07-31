### mysql.exe is a command prompt program that allows you to execute MySQL commands.

### 1. Add the system path if you have not yet added it. Usually it is located somewhere like 
> "C:\Program Files\MySQL\MySQL Workbench 8.0 CE\"

### 2. Run the command prompt
> "mysql -u root -p

### 3. Enter password
> Enter password: ******

### 4. Now you should see the prompt sign is changed into "mysql>"

### 5. List databases
> SHOW DATABASES;

### 6. Select and use a database, let's say it is called "northwind"
> USE northwind

### 7. List tables
> SHOW TABLES;

### 8. Show records from table, let's say the table name is "employees"
> SELECT * FROM employees;

### 9. If the table name contains space, you have to use "`" to enclose it, for example:
> SELECT * FROM `ibm employees`;

### 10. Exit the database
> USE mysql

### 11. Create a database and table
> CREATE DATABASE test;

> USE test

> CREATE TABLE employees (
>   id INT PRIMARY KEY AUTO_INCREMENT, 
>   name VARCHAR(255) NOT NULL, 
>   position VARCHAR(255) NOT NULL, 
>   salary FLOAT NOT NULL
> );

### 12. Insert single line record to the table
> INSERT INTO employees (
>   name, position, salary
> ) 
> VALUES (
>   "John", "CEO", 99999.99
> );

### 13. Insert multiple line of records to the table

> INSERT INTO employees (
>   name, position, salary
> ) 
> VALUES (
>   "Mary", "Manager", 9999.99
> ), (
>   "Tom", "Assistant", 999.99
> );

### 14. Update record
> UPDATE employees SET name = "Peter" WHERE id = 1;

### 15. Add Mary's salary by 10%
> UPDATE employees SET salary = salary * 1.1 WHERE name = "Mary";

### 16. Delete record
> DELETE FROM employees WHERE name = "Tom";

### 17. Delete all records
> DELETE FROM employees;

### 18. To avoid your data being deleted accidentally.

Prevent delete command being used without WHERE clause using primary key column.
> SET sql_safe_updates = 1;

Now there will be errors raised when you are trying to clear the whole table by:
> DELETE FROM employees;

Allows rollback for your action
> SET autocommit = 0;

Now you can try to delete a record like:
> DELETE FROM employees WHERE id = 1;

Then you can roll back the trasaction by:
> ROLLBACK;

### 19. To display the data in form
> USE mysql

> SELECT * FROM user \G;

### 20. Change root user password
> SET sql_safe_updates = 0;

> UPDATE mysql.user SET authentication_string=PASSWORD("new-password") WHERE user = "root";

> FLUSH PRIVILEGES;

### 21. Looping

> DELIMITER $$

> DROP PROCEDURE IF EXISTS test_while_loop$$

> CREATE PROCEDURE test_while_loop()

> BEGIN

> DECLARE i INT;

> DECLARE str VARCHAR(255);

> SET i = 1;

> SET str = "";

> WHILE i <= 5 DO

> SET str = CONCAT(str, x, ',');

> SET x = x + 1;

> END WHILE;

> SELECT str;

> END$$

> DELIMITER;
