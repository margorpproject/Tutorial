### 0. Introduction
mysql-connector is a module that allows python to communicate with MySQL. 

It is very similar to MySQL command prompt.

### 1. Installation
> pip install mysql-connector

### 2. Connect to MySQL
> from mysql.connector import connect

> conn = connect(user="<user>", passwd="<password>", host="localhost", [database="<database>"])

> cursor = conn.cursor()

### 3. List all databases
> cursor.execute("SHOW DATABASES;")

> for row in cursor:

>   print(row)

### 3. List all tables from all databases
> cursor.execute("USE mysql; SELECT table_name FROM innodb_table_stats;")

> print([row for row in cursor])

### 4. Create database
> cursor.execute("USE mysql; CREATE DATABASE IF NOT EXISTS <database_name>;")

### 5. Remove database
> cursor.execute("USE mysql; DROP DATABASE IF EXISTS <database_name>;")

> cursor.execute("USE <database_name>; DROP TABLE IF EXISTS <table_name>;")

### 6. Create table
> cursor.execute("USE <database_name>;")

> cursor.execute("CREATE TABLE <table_name> (<column_name_1> <column_type_1>, ..., <column_name_n> <column_type_n>)

> cursor.commit()

### 7. Example of creating a Employees Table
> sql = "CREATE TABLE employees (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255), position VARCHAR(255), salary FLOAT"

> cursor.execute(sql)

> cursor.commit()

### 8. Insert records to table
> cursor.execute("INSERT INTO <table_name> (<column_name_1>, ..., <column_name_n>) VALUES (<value_1>, ..., <value_n>)")

### 9. Example of adding records into Employees table
> sql = "INSERT INTO employees (name, position, salary) VALUES (%s, %s %s)"

> values = [("John","CEO",10000"), ("Mary","Manager",500), ("Tom","Office Assistant",100)]

> cursor.executemany(sql, values)

> conn.commit()

if you just have one record to add, you can simply
> cursor.execute(sql, ("John","CEO",10000))

> cursor.execute(sql, values)

### 10. Handle column name with space
To make MySQL to identify the column name with space, enclose the column name by "`".
> sql = "CREATE TABLE <table-name> (`<column_name>` <column_type>)

> cursor.execute(sql)

### 11. Error handling
> from mysql.connector import connect, Error, errorcode

> try:

> &nbsp;&nbsp;&nbsp;&nbsp;  conn = connect(host="localhost", database="<database_name>", user="<user_name>", passwd="<password>")

> &nbsp;&nbsp;&nbsp;&nbsp;  cursor = conn.cursor(prepared=True)

> &nbsp;&nbsp;&nbsp;&nbsp;  records = [(<values...>),(<values...>),(<values...>)]

> &nbsp;&nbsp;&nbsp;&nbsp;  sql = "INSERT INTO <table_name> (<columns...>) VALUES (%s, ..., %s)"

> &nbsp;&nbsp;&nbsp;&nbsp;  result = cursor.executemany(sql, records)

> &nbsp;&nbsp;&nbsp;&nbsp;  conn.commit()

> &nbsp;&nbsp;&nbsp;&nbsp;  print("Number of records being imported:", cursor.rowcount)

> except Error as error:

> &nbsp;&nbsp;&nbsp;&nbsp;  print("Error occurs: {}".format(error))

> finally:

> if (conn.is_connected()):

> &nbsp;&nbsp;&nbsp;&nbsp;  cursor.close()

> &nbsp;&nbsp;&nbsp;&nbsp;  conn.close()

> &nbsp;&nbsp;&nbsp;&nbsp;  print("connection is closed")
