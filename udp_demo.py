import socket

s = socket.socket()
host = '192.168.43.240'
port = 7890
print("server will ",host)
s.bind((host,port))
print('server created')
s.listen(1)
con , adr = s.accept()
print(adr,'is connected')
while(1):
    msg = input('->')
    msg = msg.encode()
    con.send(msg)
    print('\n')
    inc = con.recv(1024)
    inc = inc.decode()
    print('client says ',inc)
    print('\n')
