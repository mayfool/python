

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('openbarrage.douyutv.com',8601))

print( s.recv(10))




s.close()