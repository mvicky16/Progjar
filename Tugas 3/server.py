import socket
import time
import os
import shutil
import sys
from threading import Thread
import glob

server_address = ("localhost", 10000)
fn = glob.glob('*')

def reqls():
	thread = Thread(target=List, args=(connection,))
	thread.start()

def List(server_address):
#	addr = (server_address)
	connection.sendall('listing')
	for namafile in fn:
		connection.sendall(namafile)
	connection.sendall('stop_listing')

def reqdl():
#	temp = str(data)
#	if data == "sambung":
	thread = Thread(target=sendImg, args=(connection,))
	thread.start()

def sendImg(server_address):
	#addr = (server_address)
	for x in fn:
		print "Mengirim File %s" % x
		connection.sendall("masuk")
		connection.sendall(x)
		f = open(x, "rb")
		data = f.read()
		connection.sendall(data)
		time.sleep(0.02)
	print "----------------------------"
	connection.sendall("done")
	
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(server_address)

sock.listen(1)
print >> sys.stderr, "waiting connection"
connection, client_address = sock.accept()
print >> sys.stderr, "connection from", client_address

while True:
		data = connection.recv(1024)
		if str(data) == 'ls':
			reqls()
		elif str(data) == 'download':
			reqdl()