import sys
import socket
import threading
import os

usage = "python3 port.py TARGET START_PORT END_PORT"


os.system("figlet -f mono12 KRUTIK | lolcat")
print("="*50)
print("Python Simple Prot Scaner")
print ("Author  : KRUTIK")
print ("contact : http://we.me/+917600354912")
print("="*50)

if(len(sys.argv) != 4):
    print(usage)
    sys.exit()

try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Name resolution error")
    sys.exit()

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

os.system("clear")
os.system("figlet -f mono9 Running | lolcat")
print("Scanning Target : ",target)

def scan_port(port):
    #print("Scanning port:",port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    conn = s.connect_ex((target, port))
    if(not conn):
        print("Port {} is Open".format(port))
    s.close()

for port in range(start_port,end_port+1):
    thread = threading.Thread(target = scan_port, args = (port,)) 
    thread.daemon = True
    thread.start()
