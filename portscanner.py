import socket
import termcolor

def scan(target, ports):
	'''
	This function scans a target for open ports.
	
	:param target: The IP address of the target
	:param ports: The number of ports to scan
	'''
	print('\n' + ' Starting Scan For ' + str(target))
	for port in range(1,ports):
		scan_port(target,port)



def scan_port(ipaddress, port):
	'''
	This function takes in an ip address and a port number and attempts to connect to that port on the
	ip address. 
	If the connection is successful, the function will print "[+] Port Opened" and the port number. 
	If the connection is unsuccessful, the function will print nothing.
	
	:param ipaddress: The IP address of the target
	:param port: The port to scan
	'''
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		print("[+] Port Opened " + str(port))
		sock.close()
	except:
		pass


# The code above is a simple port scanner that uses the socket module to connect to a target host on a
# specified port.
targets = input("[*] Enter Targets To Scan(split them by ,): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))
if ',' in targets:
	print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)
else:
	scan(targets,ports)
