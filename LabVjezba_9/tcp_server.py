#tcp_server.py
import socket
import ssl
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 7242
s.bind((host, port))
print("Waiting for connection...")
s.listen(5)
poruka = "Server Saying Hi"
byt = poruka.encode()
while True:
    conn, addr = s.accept()
    cccon = ssl.wrap_socket(conn, server_side=True, certfile="cert.pem", keyfile="key.pem")
    print("Got connection from %s" % str(addr))
    cccon.send(byt)
    cccon.close()


