import socket
import threading
import sys
import MySQLdb

bind_ip = '192.168.43.27'
bind_port = 10000

#Connection to the db
db = MySQLdb.connect( host="172.17.0.2", user="", passwd="", db="test")


#Server socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)  # max backlog of connections

print 'Listening on {}:{}'.format(bind_ip, bind_port)

# def function() :


def handle_client_connection(client_socket):
	request = client_socket.recv(1024)
	print 'Received {}'.format(request)
	
	temperature, humidity = request.split(";")

	# We start working on the database

	cur = db.cursor()
	cur.execute("INSERT INTO data( node, temperature, humidity ) VALUES (1,"+temperature+","+humidity+")")
	db.commit()
	


	client_socket.send('ACK!')
	client_socket.close()

while True:
	client_sock, address = server.accept()
	print 'Accepted connection from {}:{}'.format(address[0], address[1])


	client_handler = threading.Thread(
		target=handle_client_connection,
		args=(client_sock,)  
	)

	client_handler.start()

db.close()
