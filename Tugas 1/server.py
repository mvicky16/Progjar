import sys
import socket

#create tcp/ip socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the socket to the port
server_address = ("localhost", 10000)
print >> sys.stderr, "starting up o %s port %s" % server_address
sock.bind(server_address)

#listen
sock.listen(1)
while True:
	#waiting connection
	print >> sys.stderr, "waiting connection"
	connection, client_address = sock.accept()
	print >> sys.stderr, "connection from", client_address
	
	#receive data
	while True:
		data = connection.recv(32)
		print >> sys.stderr, 'received "%s"' % data
		if data:
			print >> sys.stderr, "ngirim balik"
			connection.sendall(">>" +data)
		else:
			print >> sys.stderr, "kosong", client_address
			break
	#clean up connection
	connection.close()