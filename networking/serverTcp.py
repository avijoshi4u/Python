import socket

host ="localhost"
port = 4000

#socket.AF_INET -- it measns it's using ipv4 ip,
# socket.SOCK_STREAM---> it's using TCP protocol
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# bind the socket to port and host
s.bind((host,port))

# server will start up and start listening on a particular port, 1 can vary is no of connection server is going to accept
print("Server listening on port", port)
s.listen(1)


# where it will accept client connection when a client tries to connect to a server
c,addr = s.accept()
print("connection from", str(addr))

# convert string to binary format
c.send(b"Hello how are you?")
c.send("Cool".encode())
c.close()