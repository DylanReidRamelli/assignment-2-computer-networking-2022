import socket
import send
import sys

TCP_IP = '162.243.73.199'
TCP_PORT = 9993 
Buffer_Size = 1024

username = 'dylan.reid.ramelli'
username2 = 'kirustika.mohanathas'

if len(sys.argv) == 2:
    username = sys.argv[1]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

data =  s.recv(Buffer_Size)
data =  data.decode()
A = data.split(" ")
for i in range(len(A)):
    if "\n" in A[i]:
        A[i] = A[i].strip()

def estRTT(alpha, estRTT, sampleRTT):
    alpha = float(alpha)
    estRTT = int(estRTT)
    sampleRTT = int(sampleRTT)
    return int((1-alpha)*estRTT + alpha*sampleRTT)

current_estimated_rtt = A[0]
alpha = A[1]
last_rtt = A[2]
current_estimated_rtt = current_estimated_rtt.strip("ms")
last_rtt = last_rtt.strip("ms")

result = estRTT(alpha,current_estimated_rtt,last_rtt)
result = str(result)
print(result)

s.send(result.encode())

data =  s.recv(Buffer_Size)
data = data.decode().strip('\n')
print(data)

send.send_flag(username,4,data)
s.close()