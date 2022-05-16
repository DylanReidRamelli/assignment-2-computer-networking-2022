import socket 
import send
import sys
TCP_IP = '162.243.73.199'
TCP_PORT = 9995 
Buffer_Size = 1024

username = 'dylan.reid.ramelli'
username2 = 'kirustika.mohanathas'

if len(sys.argv) == 2:
    username = sys.argv[1]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

s.send(bytes("SYN Seq=0", 'utf-8'))
print("SYN Seq=0")

data =  s.recv(Buffer_Size)
data =  data.decode()

print(data.replace("\n", ""))

A= []
A = data.split(" ")

if A[0] == "SYN,ACK":
    print("ACK Seq=1 Ack=1")
    s.send(bytes("ACK Seq=1 Ack=1", 'utf-8'))
    data =  s.recv(Buffer_Size)
    data = data.decode().strip('\n')
    print(data)

    send.send_flag(username,6,data)
s.close()