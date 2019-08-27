#! /usr/bin/python3
import threading 
import socket
import time
import sys
from queue import Queue
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-T","--Target",help="define the target")
parser.add_argument("-p","--port",help="define the ports to run")

args = parser.parse_args()
if args.Target:
	targets = args.Target
else:
	targets = "localhost"

queue = Queue()
#common known ports will be identified by their names
known_ports = {
	21:"FTP",
	22:"SSH",
	23:"telnet",
	25:"SMTP",
	53:"DNS",
	80:"HTTP",
	443:"HTTPS",
	445:"SMB"

} 
#print(known_ports)
def portscan(port):
	try:
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		target = socket.gethostbyname(targets)
		sock.settimeout(1)
		sock.connect((target,port))
		return True

	except:
		return False
		
	finally:
		sock.close()

#TODO
#let the use define the range of ports to scan
#handle the exception such as keyboadinterrupt,unresolved hostname and conncetion error
port_default = 1024
if (args.port):
	port_run = int(args.port)
else:
	port_run = port_default

def get_ports():
	for port in range(1,port_run):
		queue.put(port)
open_ports = []
error = []
def worker():
	 	
	
	while not queue.empty():
		port = queue.get()
		
		if portscan(port):
			open_ports.append(port)
			if port in known_ports:
				print("port {}({}) is open".format(port,known_ports[port]))
			else:
				print("port {} is open".format(port))
		else:
			pass
			#we get an error from the portscn function
			
				

def run_scanner(threads):
	get_ports()
	thread_list = []
	for t in range(threads):
		thread = threading.Thread(target=worker)
		thread_list.append(thread)
	for thread in thread_list:
		thread.start()
	for thread in thread_list:
		thread.join()

#here am define the number of threads to use as 100
run_scanner(100)

if not open_ports:
	print("All scanned ports are clossed")



