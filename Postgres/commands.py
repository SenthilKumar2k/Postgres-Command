'connecting to postgres database'
#   psql -h localhost -p port -U username -d database  

'help with the psql command options, you can use' 
#   psql --help

'check current postgrseql version'
#   SELECT version();

'Exit the psql promt'
#   \q

'list of all database'
#   \l
#   \l+  (with size)

'Connect to a database'
#   \c database_name

'List of all tables in the current database'
#   \dt
#   \dt+ (with size)

'Describe a table (show columns and their type)'
#   \d tablename

'List all users'
#   \du

'show current user'
#   \du+

'List all schemas'
#   \dn

'Show current database connection info'
#   \conninfo

'show help on sql commands'
#   \h

'toggle expanded display'
#   \x
#   \x auto

'show summary of command'
#   \?

'Create a new database'
#   CREATE DATABASE db_postgres;

'Drop database'
#   DROP DATABASE database_name;

'Create new User'
#   CREATE USER senthil WITH PASSWORD 'password';

'create a superuser'
# CREATE USER username WITH SUPERUSER PASSWORD 'password';

'change a user password'
# ALTER USER username WITH PASSWORD 'new_password';

'Drop a user'
# DROP USER username;

'GRANT privileges to a user'
#   GRANT ALL PRIVILEGES ON DATABASE database_name TO user;

'REVOKE privileges to a user'
#   REVOKE ALL PRIVILEGES ON DATABASE database_name TO user;

'create new table'
# CREATE TABLE tablename (
#     column1 datatype PRIMARY KEY,
#     column2 datatype,
#     column3 datatype
# );

'drop table'
#   DROP TABLE table_name;

'Count the number of rows in a table:'
#   SELECT count(*) FROM tablename;

'insert data into a table'
#   INSERT INTO tablename(column1, column2, column3) VALUES(value1, value2, value3);

'add a column to a table'
#   ALTER TABLE table_name ADD COLUMN column_name datatype;

'Drop a column from a table'
#   ALTER TABLE table_name DROP COLUMN column_name;

'Rename a column'
#   ALTER TABLE table_name RENAME COLUMN old_column_name TO new_column_name;

'Rename a table'
#   ALTER TABLE old_table_name RENAME TO new_table_name;

'change the columns data type'
#   ALTER TABLE table_name ALTER COLUMN column_name TYPE new_datatype;

'set default value for a column'
#   ALTER TABLE table_name ALTER COLUMN column_name SET DEFAULT default_value;

'remove a default value for a column'
#   ALTER TABLE table_name ALTER COLUMN column_name DROP DFAULT;

'select data from the table'
#   SELECT * FROM tablename;
#   SELECT column1, column2 FROM tablename WHERE condition;

'Select distinct values'
# SELECT DISTINCT column_name FROM table_name;

'Update data in a table'
#   UPDATE tablename SET column1=value1, column2=value2 WHERE condition;

'Delete data in a table'
#   DELETE FROM tablename WHERE condition;

'import data from a csv file'
#   \copy tablename FROM 'path/to/file.csv' DELIMITER ',' CSV HEADER;

'Export a data to a CSV file'
#   \copy (SELECT * FROM tablename) TO 'path/to/file.csv' DELIMITER ',' CSV HEADER;

'Using joins (inner join)'
# SELECT a.column1, b.column2 FROM table1 a INNER JOIN table2 b ON a.common_column = b.common_column;

'Using left join'
# SELECT a.column1, b.column2 FROM table1 a LEFT JOIN table2 b ON a.common_column = b.common_column;

'Using right join'
# SELECT a.column1, b.column2 FROM table1 a RIGHT JOIN table2 b ON a.common_column = b.common_column;

'database dump'
#pg_dump -Fc -h 127.0.0.1 -U postgres -d ecommerce_db -f /home/pga/Documents/DJANGO/OWN\ PROJECTS/E-commerce/ecompro/ecommerce_db.dump

'restore database dump'
#pg_restore -d ecommerce_db -h 127.0.0.1 -U postgres ecommerce_db.dump


# Transaction Management
'Begin a transaction'
# BEGIN;
'Commit a transaction'
# COMMIT;
'Rollback a transaction'
# ROLLBACK;