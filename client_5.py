import socket
import send

#A[0] = L value
#A[1] = mb, kb,...
#A[2] = R1 value
#A[3] = mb, kb, ...
#A[4] = R2 value...
#...
#bits, Kb, Mb, Gb, Kbps, Mbps, Gbps
bits = 'bits'
kb = 'Kb'
mb = 'Mb'
gb = 'Gb'
kbps = 'Kbps'
mbps = 'Mbps'
gbps = 'Gbps'

def transmission_delay(A):
    L = int(A[0])
    R1 = int(A[2])
    R2 = int(A[4])
    # You can reuse code written in each if/elif block using a function
    if A[1] == bits:
        if A[3] == mbps:
             L = L * 0.000001
             td1 = L/R1
             td2 = L/R2
             return td1 + td2
        elif A[3] == kbps:
            L = L * 0.001
            td1 = L/R1
            td2 = L/R2
            return td1 + td2
        elif A[3] == gbps:
            L = L * 0.000000001
            td1 = L/R1
            td2 = L/R2
            return td1 + td2
    elif A[1] == kb:
        if A[3] == mbps:
             L = L * 0.001
             td1 = L/R1
             td2 = L/R2
             return td1 + td2
        elif A[3] == kbps:
            td1 = L/R1
            td2 = L/R2
            return td1 + td2
        elif A[3] == gbps:
            L = L * 0.000001
            td1 = L/R1
            td2 = L/R2
            return td1 + td2
    elif A[1] == mb:
        if A[3] == mbps:
             td1 = L/R1
             td2 = L/R2
             return td1 + td2
        elif A[3] == kbps:
            L = L * 1000
            td1 = L/R1
            td2 = L/R2
            return td1 + td2
        elif A[3] == gbps:
            L = L * 0.001
            td1 = L/R1
            td2 = L/R2
            return td1 + td2
    elif A[1] == gb:
        if A[3] == mbps:
            L = L * 1000
            td1 = L/R1
            td2 = L/R2
            return td1 + td2
        elif A[3] == kbps:
            L = L * 1000000
            td1 = L/R1
            td2 = L/R2
            return td1 + td2
        elif A[3] == gbps:
            td1 = L/R1
            td2 = L/R2
            return td1 + td2

TCP_IP = '162.243.73.199'
TCP_PORT = 9994 
Buffer_Size = 1024

username = 'dylan.reid.ramelli'
username2 = 'kirustika.mohanathas'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

data =  s.recv(Buffer_Size)
data =  data.decode()
print(data.replace("\n", ""))

A= []
A = data.split(" ")
for i in range(len(A)):
    if "\n" in A[i]:
        A[i] = A[i].strip()

A[0] = A[0].strip('L=')
A[2] = A[2].replace('R1=', '')
A[4] = A[4].replace('R2=', '')
message = bytes(str(transmission_delay(A)), 'utf-8')
s.sendall(message)
data =  s.recv(Buffer_Size)
data = data.decode().strip('\n')
print(data)

send.send_flag(username,5,data)

s.close()