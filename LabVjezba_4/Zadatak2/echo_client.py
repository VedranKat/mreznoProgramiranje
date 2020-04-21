# -- coding: utf-8 --
#echo_client.py
import socket

host = socket.gethostname()
port = 12345
client_socket = socket.socket()
client_socket.connect((host,port))
msg = "Teskt koji se salje serveru"
byt = msg.encode()
client_socket.sendall(byt)
data = client_socket.recv(1024)

print (str(data))
client_socket.close()