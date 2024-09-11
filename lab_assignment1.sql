mysql> Create database Bank;
Query OK, 1 row affected (0.05 sec)

mysql> Show databases;
+-------------------------+
| Database                |
+-------------------------+
| bank                    |
| company                 |
| ecommerce               |
| employee                |
| information_schema      |
| librarydb               |
| mysql                   |
| performance_schema      |
| sales                   |
| studentmanagementsystem |
| sys                     |
+-------------------------+
11 rows in set (0.02 sec)

mysql> Use Bank;
Database changed
mysql> Create Table bankaccount(
    -> account_id INT PRIMARY KEY,
    ->  account_holder_name VARCHAR(100),
    ->  account_balance DECIMAL(15,2)
    -> );
Query OK, 0 rows affected (0.07 sec)

Task 1 : 

mysql> INSERT INTO bankaccount(account_id,account_holder_name,account_balance)
    -> VALUES
    -> (101,'Prem Kadam',50000),
    -> (102,'Aniket Phalke',45000),
    -> (103,'Tejas Bhujvadkar',35000),
    -> (104,'Sujal Patil',25000);
Query OK, 4 rows affected (0.02 sec)
Records: 4  Duplicates: 0  Warnings: 0

Task 2 : 

mysql> Select account_holder_name,account_balance from bankaccount;
+---------------------+-----------------+
| account_holder_name | account_balance |
+---------------------+-----------------+
| Prem Kadam          |        50000.00 |
| Aniket Phalke       |        45000.00 |
| Tejas Bhujvadkar    |        35000.00 |
| Sujal Patil         |        25000.00 |
+---------------------+-----------------+
4 rows in set (0.00 sec)

Task 3 : 

mysql> Select account_holder_name,account_balance from bankaccount
    -> where account_balance > 30000;
+---------------------+-----------------+
| account_holder_name | account_balance |
+---------------------+-----------------+
| Prem Kadam          |        50000.00 |
| Aniket Phalke       |        45000.00 |
| Tejas Bhujvadkar    |        35000.00 |
+---------------------+-----------------+
3 rows in set (0.00 sec)

Task 4 : 

mysql> Update bankaccount
    -> SET  account_balance = 47000
    -> where account_id=101;
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> Select * from bankaccount;
+------------+---------------------+-----------------+
| account_id | account_holder_name | account_balance |
+------------+---------------------+-----------------+
|        101 | Prem Kadam          |        47000.00 |
|        102 | Aniket Phalke       |        45000.00 |
|        103 | Tejas Bhujvadkar    |        35000.00 |
|        104 | Sujal Patil         |        25000.00 |
+------------+---------------------+-----------------+
4 rows in set (0.00 sec)
