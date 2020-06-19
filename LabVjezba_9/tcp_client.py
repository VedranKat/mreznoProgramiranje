#tcp_client.py
import socket
import ssl
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 7242
ssl_cs = ssl.wrap_socket(cs, ca_certs="cert.pem", cert_reqs = ssl.CERT_REQUIRED)
ssl_cs.connect((host,port))
tm = ssl_cs.recv(1024)
print(tm)
ssl_cs.close()
