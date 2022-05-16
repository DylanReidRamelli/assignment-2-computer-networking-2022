import socket
TCP_IP = '162.243.73.199'
TCP_PORT = 11111
Buffer_Size = 102400

username = 'dylan.reid.ramelli'
username2 = 'kirustika.mohanathas'


# Send flag received back to server
def send_flag(username, assignment_n, flag):
	assignment_n = str(assignment_n)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	s.send((username + " " + assignment_n + " " + flag).encode())
	data = s.recv(Buffer_Size)
	print(data.decode().strip('\n')) 
	s.close() 
