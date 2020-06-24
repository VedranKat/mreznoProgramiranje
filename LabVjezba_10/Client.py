import datetime
import socket
import sys


komp = socket.gethostname()
print ("Program pokrenut datuma " + str(datetime.datetime.now()) + " na računalu " + str(komp))

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((komp,7242))

print("Upisite ime i prezime")
msg = input("Unos >>")

def Main():

    while True: 
        s.send(msg.encode('ascii'))

        data=s.recv(1024)
    
        print('Server vraća: ', str(data.decode('ascii')))    
        inp=input('Upisite exit za ugasit program  ')

        if inp =='exit':
            print("Bye")
            break
        else:
            continue
        s.close()

if msg =='Vedran Katavic':
    Main()
else:
    print("Krivo ime i prezime")
    