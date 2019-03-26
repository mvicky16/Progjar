import socket
import select

IP = "127.0.0.1"
PORT = 9000
timeout = 3

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(fn, (IP, PORT))

while True:
    n, addr = sock.recvfrom(1024)
    if n:
        print "File name:", n
        fn = n.strip()

    f = open(fn, 'wb+')

    while True:
        ready = select.select([sock], [], [], timeout)
        if ready[0]:
            n, addr = sock.recvfrom(1024)
            f.write(n)
        else:
            print "%s Finish!" % fn
            f.close()