import socket 
import datetime
from _thread import *
import threading


print ("Program pokrenut datuma " + str(datetime.datetime.now()))


plock= threading.Lock()

def threaded(c):
    while True:
        
        data=c.recv(1024)

        if not data:
            print('Exiting')
            
            plock.release()
            break
        
        c.send(data)
        
    c.close()

def Main():
    host=""
        
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,7242))  
    s.listen(5)
    print("Socket sluša")
    
    while True:

        c,addr=s.accept()
        
        plock.acquire()

        print('Connected : ' , addr[0], ':' , addr[1])
        
        start_new_thread(threaded, (c,))
    s.close()

if __name__=='__main__':
    Main()