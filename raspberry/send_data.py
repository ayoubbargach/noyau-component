import subprocess


def execute_command( bashcommand ) :

	process = subprocess.Popen( bashcommand.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()

	return output

print( execute_command(  "mysql -uroot -p123456 -h 172.17.0.2 -P 3306 -e \"CREATE DATABASE test;\"" ))
print( execute_command(  "mysql -uroot -p123456 -h 172.17.0.2 -P 3306 test -e \"CREATE TABLE test (id int, nom varchar(255) );\"" ))


# The part where we insert the data
print( execute_command(  "mysql -uroot -p123456 -h 172.17.0.2 -P 3306 test -e \"INSERT INTO test VALUES(23, 'test2');\"" ))


