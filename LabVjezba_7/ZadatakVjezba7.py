from errno import ECONNREFUSED
from functools import partial
from multiprocessing import Pool
import multiprocessing as mp
import socket
import time
import datetime

def ping(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        print(str(port) + " - Otvoren") 
        s.close()               
    except Exception:        
        s.close()
        pass


def scan_ports(host):
    od = input('Pocetni port: ')
    do = input('Zadnji port: ')
    p = Pool(mp.cpu_count()*2)
    ping_host = partial(ping, host)
    p.map(ping_host, range(int(od), int(do)))


def main():      
    print("Program je pokrenut na računalu:")
    print (socket.gethostname())
    print ("Program pokrenut u:")
    print (datetime.datetime.now())
    
    PocetnoVrime = time.time()
    target = input('Unesite adresu: ')
    
    host = socket.gethostbyname(target)
    socket.setdefaulttimeout(0.55)
    
        
    scan_ports(host)   
    trajanje = float("%0.3f" % (time.time() - PocetnoVrime))
    print("Skeniranje je trajalo: ", trajanje, "sekunde")


if __name__ == "__main__":
    main()