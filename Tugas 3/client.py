import socket
import sys
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dn = '2%s'
server_address = ('localhost', 10000)
sock.connect(server_address)

while True:
	cmd = raw_input('Command :')	
	sock.sendall(cmd)
	data = sock.recv(1024)
	#a = sock.recv(1024)
	if cmd == 'exit':
		break
		
	elif cmd == 'ls':
		print 'List Files :'
		temp = sock.recv(1024)
		if str(temp) == 'stop_listing':
			break
		else:
			print temp+ '\n'
	
	elif cmd == 'download':
		while True:
			a = sock.recv(1024)
			if a == 'masuk':
				namafile = sock.recv(1024)
				f = open(dn % namafile, 'wb+')
				b = sock.recv(20480)
				f.write(b)
				f.close()
				print "File "+ namafile+ " telah diterima"
			if a == 'done':
				break
	else:
		print 'Command yang benar!'
		
sock.close()