The InnoDB cluster 'sandboxCluster' is available on the following ports:

     localhost:3310 through localhost:3330

To connect with MySQL Shell execute the following command:

     mysqlsh root@localhost:3310

To bootstrap MySQL Router execute the following command:

     mysqlrouter --bootstrap root@localhost:3310 --directory router-sandbox
