import socket
import send
TCP_IP = '162.243.73.199'
TCP_PORT = 9999
Buffer_Size = 1024

username = 'dylan.reid.ramelli'
username2 = 'kirustika.mohanathas'


# Got this method grom geekforgeeks.
def sum(a, b):
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    # Initialize the result
    result = ''

    # Initialize the carry
    carry = 0

    # Traverse the string
    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result

        # Compute the carry.
        carry = 0 if r < 2 else 1

    if carry != 0:
        result = '1' + result
    return result


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

data = s.recv(Buffer_Size)
data = data.decode()
print(data.replace("\n", ""))

A = []
A = data.split(" ")


# result = bin(int(A[0],2) + int(A[1],2))
# result = str(result)
result = sum(A[0], A[1])
result = result[:len(result)-1]
final_result = ''
print(result)
for i in result:
    if i == '0':
        final_result += '1'
    elif i == '1':
        final_result += '0'

print(final_result)

s.send(final_result.encode())
data =  s.recv(Buffer_Size)
data = data.decode().strip('\n')
print(data)

send.send_flag(username,10,data)


s.close()
