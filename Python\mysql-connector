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

### 4. Create database and table
> cursor.execute("USE mysql; CREATE DATABASE IF NOT EXISTS <database_name>;")

> cursor.execute("USE <database_name>; CREATE TABLE IF NOT EXISTS <table_name>;")

### 5. Remove database and table
> cursor.execute("USE mysql; DROP DATABASE IF EXISTS <database_name>;")

> cursor.execute("USE <database_name>; DROP TABLE IF EXISTS <table_name>;")

