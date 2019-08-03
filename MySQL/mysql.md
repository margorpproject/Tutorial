### mysql.exe is a command prompt program that allows you to execute MySQL commands.

### 1. Add the system path if you have not yet added it. Usually it is located somewhere like 
> "C:\Program Files\MySQL\MySQL Workbench 8.0 CE\"

### 2. Run the command prompt
> "mysql -u root -p

Enter password
> Enter password: ******

Now you should see the prompt sign is changed into "mysql>"
> mysql>

### 3. Initialize root password if neccessary
> USE mysql;

> UPDATE user SET authentication_string=PASSWORD("yourpassword") WHERE user="root";

> UPDATE user SET plugin="mysql_native_password" WHERE user="root";

> FLUSH PRIVILEGES;

Don't forget to restart the mysql server from console or terminal

For Linux:
> sudo service mysql restart

### 4. Change database or table charset to utf8
> ALTER DATABASE dbname CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

> ALTER TABLE tablename CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

If the above commands not solving your problem, you may try
> ALTER DATABASE dbname CHARACTER SET utf8 COLLATE utf8_general_ci;

> ALTER TABLE tablename CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;

The difference between utf8mb4 and utf8 is the first one supports most of 4-byte unicode while utf8 only supports 3 byte unicode. If you still find error in encoding issure for utf8mb4, try the following command:

> SET NAMES utf8mb4 COLLATE utf8mb4_unicode_ci;

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

change default delimiter from ";" to "$$", so you can use ";" in your code without exit the program.
> DELIMITER $$

make sure you have deleted the procedure before you create a new one
> DROP PROCEDURE IF EXISTS test_while_loop$$

> CREATE PROCEDURE test_while_loop()

start your program
> BEGIN

> DECLARE i INT;

> DECLARE str VARCHAR(255);

> SET i = 1;

> SET str = "";

> WHILE i <= 5 DO

> SET str = CONCAT(str, i, ',');

> SET i = i + 1;

> END WHILE;

display the result
> SELECT str;

> END$$

change back the delimiter to default character ";"
> DELIMITER ;
