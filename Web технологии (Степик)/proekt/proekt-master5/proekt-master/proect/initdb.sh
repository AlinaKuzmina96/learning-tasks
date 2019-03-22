sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE djbase;"
mysql -uroot -e "GRANT ALL PRIVILEGES ON djbase.* TO 'box'@'localhost' WITH GRANT OPTION;"
