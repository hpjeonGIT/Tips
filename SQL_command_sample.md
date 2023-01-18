# Oracle SQL
- All schema names  
SELECT USERNAME FROM ALL_USERS  
- All view names  
SELECT VIEW_NAME FROM ALL_VIEWS  
- All table names in a schema  
SELECT TABLE_NAME FROM  ALL_TABLES WHERE OWNER='MYSCHEMA'  
- All view names in a schema  
SELECT VIEW_NAME FROM  ALL_VIEWS WHERE OWNER='mySCHEMA'  
- Find View Names containing words  
SELECT VIEW_NAME FROM ALL_VIEWS WHERE VIEW_NAME LIKE '%ENGINE%'  
- Find column names from a view  
SELECT column_name FROM all_tab_columns WHERE table_name='SOME_VIEW'  
- Pull data with limited amount  
SELECT * FROM MYSCHEMA.HIS_VIEW WHERE rownum <= 5  
- Pull data with time range  
SELECT DATA_HIRED, X, Y, Z FROM MYSCHEMA.HER_VIEW WHERE DATA_HIRED BETWEEN to_date('2018-Dec-19 10:00:00','yyyy-mon-dd hh24:mi:ss') AND to_date('2018-Dec-29 10:00:00','yyyy-mon-dd hh24:mi:ss') ORDER BY DATA_HIRED ASC  


## mysql
- Allowing IPs to be accessible
- sudo mysql -u root -p
- SELECT host FROM mysq.user WHERE User = 'mydb';
```
+------------+
| host       |
+------------+
| some IP    |
| local host |
+------------+
```
- CREATE USER 'mydb'@'some_IP' IDENTIFIED BY 'passwd';
- GRANT ALL PRIVILEGES ON *.* to 'mydb'@'some_IP';
- FLUSH PRIVILEGES;
- SELECT host FROM mysq.user WHERE User = 'mydb'; # check if the new IP is added
