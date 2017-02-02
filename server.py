#!/usr/bin/env python
import socket               # Import socket module
import sys
s = socket.socket()         # Create a socket object
#host = socket.gethostname() # Get local machine name
host = "192.168.60.150"
port = 12345                 # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
f = open('torecv.png','wb')
s.listen(5)                 # Now wait for client connection.
while True:
    c, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    print "Receiving..."
    l = c.recv(1024)
    #ll = dict(l)
    method = l
    if method == "PUT":
        c.send("OK")
        filename = c.recv(1024)
        print(">>" + filename )
        c.send("Aok")
        f = open(filename , 'wb')
        l = c.recv(1024)
        while (l):
            print "Receiving..."
            f.write(l)
            l = c.recv(1024)
        f.close()
    elif method == "GET":
        c.send("ready")
        l = c.recv(1024)
        print(l)
        with open(l) as f:
            print 'Sending...'
            print(f )
            for line in f:
                print(line)			    
                s.sendall(line)
        s.shutdown(socket.SHUT_WR)
    print "Done Receiving"
    c.send('Dok')
    c.close()
