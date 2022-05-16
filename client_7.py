import socket 
import random
import send
TCP_IP = '162.243.73.199'
TCP_PORT = 9996 
Buffer_Size = 1024

username = 'dylan.reid.ramelli'
username2 = 'kirustika.mohanathas'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

Seq = random.randint(1,10)
Ack = random.randint(1,10)
message = "FIN,ACK Seq=%d Ack=%d" % (Seq, Ack)

s.send(bytes(message, 'utf-8'))
print(message)


data =  s.recv(Buffer_Size)
data =  data.decode()
print(data.replace("\n", ""))

A = []
A = data.split(" ")


if A[1].endswith(str(Ack)):
    ack_seq_value = A[len(A)-1]
    ack_seq_value = ack_seq_value.replace("Ack=", "")
    ack_seq_value = ack_seq_value.replace("\n", "")
    ack_value = int(A[3].replace("Seq=", ""))
    message = "ACK Seq=%s ACK=%d" % (ack_seq_value, ack_value + 1)
    s.send(bytes(message, 'utf-8'))
    print(message)
    data =  s.recv(Buffer_Size)
    data = data.decode().strip('\n')
    print(data)

    send.send_flag(username,7,data)

s.close()