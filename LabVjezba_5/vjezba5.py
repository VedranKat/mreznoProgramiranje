import datetime
import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
stTime = time.time()

print("Program je pokrenit na računalu:")
print (socket.gethostname())
print ("Program pokrenut u:")
print (datetime.datetime.now())

print ("-")
print ("Unesite adresu:")
target = input("Adresa >> ")
targetIP = socket.gethostbyname(target)
print ("Skeniram host %s, IP adresu: %s" % (target, targetIP))
start = input("Startni port >> ")
end = input("Zadnji port >> ")

def scanner(port):
    try:
        sock.connect((target,port))
        return True
    except:
        return False
    

for portNumber in range(int(start), int(end)+1):
 print("Skenira port: ", portNumber)
 if(scanner(portNumber)):
    print("Port: ", portNumber, " je otvoren.")
 else:
    print("Port: ", portNumber, "nije otvoren")

time=time.time()-stTime
print(time)