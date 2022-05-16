import socket 
import send
import sys

UDP_IP = '162.243.73.199'
UDP_PORT = 9991 
message = b"helo"
buffer_Size = 1024

username = 'dylan.reid.ramelli'
username2 = 'kirustika.mohanathas'

if len(sys.argv) == 2:
	username = sys.argv[1]


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(message, (UDP_IP,UDP_PORT))
print(message.decode())
data = s.recv(buffer_Size)
data = data.decode().strip('\n')
print(data)

send.send_flag(username,2,data)

s.close()
