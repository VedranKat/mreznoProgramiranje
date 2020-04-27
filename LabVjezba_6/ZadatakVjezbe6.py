import socket
import time 
import threading  
import datetime
from queue import Queue 

socket.setdefaulttimeout(0.55)
p_lock = threading.Lock()

print("Program je pokrenut na računalu:")
print (socket.gethostname())
print ("Program pokrenut u:")
print (datetime.datetime.now())
PocetnoVrime = time.time()

target = input('Unesite adresu: ')

t_IP = socket.gethostbyname(target)
od = input('Pocetni port: ')
do = input('Zadnji port: ')

def ports(port):   
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
   try:      
      con = sock.connect((t_IP, port)) 
      with p_lock:
         print(port, 'je otvoren')  
      con.close()
   except:
      pass

def threads():
   while True:    
      worker = q.get()      
      ports(worker)      
      q.task_done()     

q = Queue()
 
for x in range(200):   
   t = threading.Thread(target = threads)
   t.daemon = True
   t.start()

for worker in range(int(od), int(do)):
   q.put(worker)
  
q.join()
trajanje = float("%0.3f" % (time.time() - PocetnoVrime))
print("Skeniranje je trajalo: ", trajanje, "sekunde")