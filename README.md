# python

import socket


s =socket.socket()

print('socket created')
s.bind(('10.100.3.191',9998))

s.listen(3)

print('waiting for connectins')

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print('connected with ',addr, name)

    c.send(bytes('welcome to isthara','utf-8'))

    c.close()
    

