import socket
import sys
import send
TCP_IP = '162.243.73.199'
TCP_PORT = 9997
Buffer_Size = 1024

username = 'dylan.reid.ramelli'
username2 = 'kirustika.mohanathas'


# Found this on stack. 
# https://stackoverflow.com/questions/2733788/convert-ip-address-string-to-binary-in-python
def ip2bin(ip):
    octets = map(int, ip.split('/')[0].split('.'))
    binary = '{0:08b}{1:08b}{2:08b}{3:08b}'.format(*octets)
    range = int(ip.split('/')[1]) if '/' in ip else None
    return binary[:range] if range else binary

def ip_format(ip):
	return ".".join(map(str, int(ip, 2).to_bytes(4, "big")))


def AND_OP(s1, s2):
	res = ""
	for i in range(len(s1)):
		res = res + str(int(s1[i]) & int(s2[i]))
	return res

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

data = s.recv(Buffer_Size)
data = data.decode()
print(data)
result = data.strip('\n').split(' ')

net_mask = ''
ones = int(result[1])

for i in range(0,32):
	if i <= ones:
		net_mask += '1' 
	else:
		net_mask+='0'



A = result[0].split('.')

binary_ip = ip2bin(result[0])

super_result = AND_OP(binary_ip,net_mask)
super_result = ip_format(super_result)

s.send(super_result.encode())

data = s.recv(Buffer_Size)
data = data.decode().strip('\n')
print(data)

send.send_flag(username,8,data)

s.close()
