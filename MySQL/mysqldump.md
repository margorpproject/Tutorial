mysqldump.exe is a program that allows database inside MySQL to export into sql text.

1. open cmd

2. test if mysqldump is accessible

> mysqldump --version

If mysqldump is not found, you have to find the location of mysqldump.exe and add the folder path into system path. For Windows, the program should be found in:

> c:\Program Files\MySQL\MySQL Workbench 8.0 CE

If you have no permission to change system path, you can directly call the program as below.

> "c:\Program Files\MySQL\MySQL Workbench 8.0 CE\mysqldum.exe" --version

3. Exampe:

source database name:
> source_db

target file path:
> C:\MySQL\source_db.sql

command:
> "c:\Program Files\MySQL\MySQL Workbench 8.0 CE\mysqldump.exe" --user=root --host=localhost --protocol=tcp --port=3306 --default-character-set=utf8 --single-transaction=TRUE --column-statistics=0 --skip-triggers -p "source_db" > "C:\MySQL\source_db.sql"

> Enter password: ******

4. Note --column-statistic is introduced in version 8.x, so if you have earlier version, you can remove the argument.
