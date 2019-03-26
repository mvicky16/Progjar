import socket
import time
import sys
import os

IP = "127.0.0.1"
PORT = 9000
timeout = 3

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto('sambung', (IP, PORT))
dn = 'Client3/%s'

while True:
	a, addr = sock.recvfrom(1024)
	if a == "done":
		break
	if a == ('masuk'):
		namafile, addr = sock.recvfrom(1024)
		f = open(dn % namafile, 'wb+')
		b, addr = sock.recvfrom(20480)
		f.write(b)
		f.close()
		print "File "+ namafile+ " telah diterima"
		
sock.close()

