import socket

s= socket.socket()

# client connect to the host and port on which server is listening
s.connect(("localhost",6000))
filename = input("Enter the file name")
s.send(filename.encode())
content = s.recv(1024)
print(content.decode())



s.close()
