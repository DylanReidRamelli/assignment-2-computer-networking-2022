import socket
import send
import sys
TCP_IP = '162.243.73.199'
TCP_PORT = 9992 
Buffer_Size = 1024
username = 'dylan.reid.ramelli'
username2 = 'kirustika.mohanathas'

if len(sys.argv) == 2:
	username = sys.argv[1]



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
random_port = s.recv(Buffer_Size)
random_port = random_port.decode()
print(random_port.replace("\n", ""))
A = random_port.split(" ")
x = int(A[2])
s.close()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, x))
data = s.recv(Buffer_Size)
data = data.decode().strip('\n')
print(data)

send.send_flag(username,3,data)