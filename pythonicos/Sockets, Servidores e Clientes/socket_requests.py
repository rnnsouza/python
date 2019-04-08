# -*- coding:utf-8 -*-

# Requisitando Servidor Web com Sockets

import socket
import sys

# Argumento 0 é sempre o nome do programa, sys.argv[0]
host = sys.argv[1]
path = sys.argv[2] if len(sys.argv) >= 3 else "" # Operador Ternário

msg = ("GET /%s HTTP/1.1\nHost: %s\n\n" % (path,host)).encode()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)

print("Conectado")
s.connect((socket.gethostbyname(host),80)) # Tudo dentro de uma tupla

print("Enviando")
s.send(msg)

print("Recebendo")
data = ""
while 1:
	try:
		buf = s.recv(1024)
		data += buf
	except:
		s.close()
		break
print(data)