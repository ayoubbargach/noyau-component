import socket
import sys
import MySQLdb


if len(sys.argv) < 2 :
	ip = '0.0.0.0'
	port = 15000
	port2 = 15001
	consigne = 20

else :
	ip = '0.0.0.0'
	port = 15000
	port2 = 15001
	consigne = int(sys.argv[1])

def send_assignment( rule, ip, port ) :

	# create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# connect the client
	# client.connect((target, port))
	client.connect((ip, port))

	# send some data 
	client.send(rule)


	# receive the response data (4096 is recommended buffer size)
	# response = client.recv(4096)
	client.close();

while True :
	#Connection to the db
	db = MySQLdb.connect( host="172.17.0.2", user="root", passwd="123456", db="test")
	cur = db.cursor()
	cur.execute("SELECT * FROM data ORDER BY time DESC LIMIT 1")
	

	for row in cur.fetchall() :
		print( int(row[3]) - consigne )
		if int(row[3]) > consigne :
			send_assignment("1", ip ,port)
			send_assignment("0", ip ,port2)
		else :
			send_assignment("0", ip ,port)
			send_assignment("1", ip ,port2)
			
		

	db.close()


