import socket

HOST = '127.0.0.1'
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, address = s.accept()
print('Connected by', address)
while 1:
    data = conn.recv(1024).decode(encoding='utf_8')
    print(address, data)
    if data == 'exit':
        conn.sendall(b'bye')
        break
    else:
        conn.sendall(b'Hello')
conn.close()
