### 1. connect to mysql

first, make sure you have donwload jdbc connector from mysql.\
> https://dev.mysql.com/downloads/connector/j/5.1.html

next, create a "javaclasspath.txt" under the start directory once the matlab is started.
> cd C:\Program Files\MATLAB\R2018a\bin\win64

paste the connector jar file path in the file.\
here is an examaple:\
// C:\Program Files\MATLAB\R2018a\bin\win64\javaclasspath.txt
>C:\Program Files (x86)\MySQL\Connector J 8.0\mysql-connector-java-8.0.17.jar

restart matlab

now test the code by creating a load_data.m

// load_data.m
>function data = load_data(server, port, dbname, user, password, sql)\
>  driver = 'com.mysql.jdbc.Driver';\
>  connstr = strcat('jdbc:mysql://',server,':',num2str(port),'/',dbname,'?useSSL=false&serverTimezone=UTF');\
>  conn = database('', user, password, driver, connstr);\
>  cursor = conn.exec(sql);\
>  cursor = fetch(cursor);\
>  data = cursor.Data;\
>  cursor.close();\
>  conn.close();\
>end

