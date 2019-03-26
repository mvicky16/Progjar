import socket
import time
import os
import shutil
import sys
from threading import Thread

IP = "127.0.0.1"
PORT = 9000
fn = ['A.jpg', 'B.jpg','C.jpg']

def req():
	data, addr = sock.recvfrom(1024)
	temp = str(data)
	if data == "sambung":
		sock.sendto("client",addr)
		thread = Thread(target=sendImg, args=(addr))
		thread.start()

def sendImg(ip, port):
	addr = (ip, port)
	for x in fn:
		print "Sending %s ..." % x
		sock.sendto("masuk", addr)
		sock.sendto(x,addr)
		f = open(x, "rb")
		data = f.read()
		sock.sendto(data, addr)
		time.sleep(0.02)
	print " "
	sock.sendto("done",addr)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))

while True:
		req()