import socket
import time
import sys

IP = "127.0.0.1"
PORT = 9000
buf = 1024
fn = 'A.jpg'


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))

print "Sending %s ..." % fn

f = open(fn, "r")
n = f.read(buf)
while(n):
    if(sock.sendto(n, (IP, PORT))):
        n = f.read(buf)
        time.sleep(0.02)

sock.close()
f.close()