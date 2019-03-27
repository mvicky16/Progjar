import socket
import time
import os
import shutil
import sys
from threading import Thread

server_address = ("localhost", 10000)
fn = ['A.jpg', 'B.jpg','D.jpg']

def req():
	data, addr = connection.recv(1024)
	temp = str(data)
	if data == "sambung":
		thread = Thread(target=sendImg, args=(addr))
		thread.start()

def sendImg(server_address):
	#addr = (server_address)
	for x in fn:
		print "Mengirim File %s" % x
		sock.sendall("masuk")
		sock.sendall(x)
		f = open(x, "rb")
		data = f.read()
		sock.sendall(data)
		time.sleep(0.02)
	print "----------------------------"
	sock.sendall("done",addr)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(server_address)

sock.listen(1)
while True:
	#waiting connection
	print >> sys.stderr, "waiting connection"
	connection, client_address = sock.accept()
	print >> sys.stderr, "connection from", client_address
	
while True:
		req()