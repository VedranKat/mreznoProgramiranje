# -- coding: utf-8 --
#client.py
import socket
import datetime
import time

print (datetime.datetime.now())
host = socket.gethostname()
port = 12345
client_socket = socket.socket()
client_socket.connect((host,port))
print ("Unesite teskst koji zelite poslat serveru da ga vrati:")
msg = input("Unos >>")
byt = msg.encode()
client_socket.sendall(byt)
data = client_socket.recv(1024)

print (str(data))
client_socket.close()
