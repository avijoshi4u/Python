import socket

s= socket.socket()

# client connect to the host and port on which server is listening
s.connect(("localhost",4000))
# no of byte receive at a time
msg = s.recv(1024)

while msg:
    print("received :",msg.decode())
    msg = s.recv(1024)

s.close()
