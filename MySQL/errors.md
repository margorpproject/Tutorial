### 1. can't connect to server, 10061 (code 2003)
> open file browser and locate "C:\Program Files\MySQL\MySQL Server <version>\data"

> rename it as a backup data in case you have to restore it

> open powershell under adminitrator mode

> cd "C:\Program Files\MySQL\MySQL Server <version>\bin"

> .\mysqld --initialize

> net start mysql
