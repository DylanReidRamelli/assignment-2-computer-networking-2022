import socket
import send

TCP_IP = '162.243.73.199'
TCP_PORT = 9990 
Buffer_Size = 102400
username = 'dylan.reid.ramelli'
username2 = 'kirustika.mohanathas'


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
data = s.recv(Buffer_Size)
s.close() 
data = data.decode().strip('\n')
print(data)

send.send_flag(username, 1, data)
