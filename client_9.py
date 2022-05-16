import socket 
import send
import sys
TCP_IP = '162.243.73.199'
TCP_PORT = 9998 
Buffer_Size = 1024
username = 'dylan.reid.ramelli'
username2 = 'kirustika.mohanathas'

if len(sys.argv) == 2:
	username = sys.argv[1]


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
data = s.recv(Buffer_Size)
data = data.decode().strip('\n')

A = data.split(',')

destination_ip = A[-1]
destination_ip_interface = len(A) - 2
print(A)	
print(destination_ip)
print(destination_ip_interface)

s.send(bytes(destination_ip_interface))
data = s.recv(Buffer_Size)
data = data.decode().strip('\n')
print(data)

