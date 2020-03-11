#google.py
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "www.google.com"
port = 80
remote_ip = socket.gethostbyname(host)
print("Ip adresa hosta www.google.com je " + str(remote_ip))
s.connect((remote_ip, port))
print("Socket se uspješno spojio na Google, preko porta:"+str(port)+" na Ip Adresu: "+str(remote_ip)) 
    

