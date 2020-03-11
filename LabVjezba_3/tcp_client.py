#tcp_client.py
import socket
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 7242
cs.connect((host,port))
tm = cs.recv(1024)
print(tm)
cs.close()
