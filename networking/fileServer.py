import socket

host ="localhost"
port = 6000

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

filename = c.recv(1024)
try:
    f = open(filename,"rb")
    content = f.read()
    c.send(content)
except FileNotFoundError:
    c.send("file doesn't exist".encode())
    print("file doesn't exist")

finally:
    f.close()



c.close()