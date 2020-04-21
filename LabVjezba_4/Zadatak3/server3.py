# -- coding: utf-8 --
#server.py
import socket
import datetime
import time

print (datetime.datetime.now())
host = socket.gethostname()
port = 12345

echo_server = socket.socket()
echo_server.bind((host,port))
echo_server.listen(5)

print ("Cekam klijenta...")
conn, addr = echo_server.accept()
print ("Spojen: ", addr)
ime = "Vedran Katavic"

while True:
    data = conn.recv(1024)
    poruka = data.decode()    
    if not data:
        break
    if str(poruka) == ime:
        msg = "Taj unos nije podrzan"
        byt = msg.encode()
        conn.sendall(byt)
    else:    
        conn.sendall(data)
conn.close()

