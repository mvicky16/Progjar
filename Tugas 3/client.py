import socket
import time
import sys
import os


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dn = 'Client1/%s'
server_address = ('localhost', 10000)
sock.connect(server_address)
sock.sendall('sambung')

while True:
	a, addr = sock.recv(1024)
	if a == "done":
		break
	if a == ('masuk'):
		namafile, addr = sock.recv(1024)
		f = open(dn % namafile, 'wb+')
		b, addr = sock.recv(20480)
		f.write(b)
		f.close()
		print "File "+ namafile+ " telah diterima"
		
sock.close()

