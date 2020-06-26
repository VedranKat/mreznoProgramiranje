import dns.resolver
import socket
from dns import reversename, resolver


adresa = input("IP ADRESA>>")

dns = socket.gethostbyaddr(adresa)


revname = reversename.from_address(adresa)
ptr = str(resolver.query(revname, "PTR")[0])


print ("A: " + str(adresa))

for x in resolver.query('google.com', 'MX'):
     print("MX:" + x.to_text())

print ("PTR: " + ptr)








