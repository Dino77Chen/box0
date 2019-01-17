import socket
HOST = '127.0.0.1'
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
max_size = 1024
while 1:
    cmd = input("Please say: ")
    s.sendall(cmd.encode(encoding='utf_8'))
    data = s.recv(max_size).decode(encoding='utf_8')
    print(data)
    if data == 'bye':
        break
s.close()
