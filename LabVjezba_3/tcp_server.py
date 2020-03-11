#tcp_server.py
import socket
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
    print("Got connection from %s" % str(addr))
    conn.send(byt)
    conn.close()


