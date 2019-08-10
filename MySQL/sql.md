### Create database

Create a simple default database
> CREATE DATABASE <db-name>;

Create a database with specific encoding
> CREATE DATABASE <db-name> COLLATE <encoding_name>;

To list the encoding name
> SHOW CHARACTER SET;

Example:
> CREATE DATABASE northwind COLLATE utf8mb4_unicode_ci;

### Change encoding of an existing database

### Create table
> CREATE TABLE <db-name>.<table-name> (<column-1> <column-type-1>, ..., <column-n> <column-type-n>);

### Common column types

String with n length, where n is an integer which n > 0 and n <= 255
> VARCHAR(n)

Integer with n length, where n is an integer which n > 0 and n <= 11
> INT(n)

Primary key with auto number
> INT PRIMARY KEY AUTO_INCREMENT NOT NULL

### Set column with specific encoding
> <column-type> COLLATE <encoding-name>

example
> CREATE TABLE northwind.employees (name VARCHAR(255) COLLATE utf8mb4_unicode_ci);

