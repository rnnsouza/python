# -*- coding: utf-8 -*-

import socket

# Nome para IP
ip = socket.gethostbyname('google.com')
print(ip)

# IP para nome
dns = socket.gethostbyaddr(ip)
print(dns)

# Retorna o nome da máquina local
print(socket.gethostname())

# Retorna um serviço a partir de uma porta
service = socket.getservbyport(80)
print(service)

# Retorna a porta a patir de um serviço
port = socket.getservbyname('domain')
print(port)






### Utilidades ###

'''
socket.gethostbyname() - Nome para IP
socket.gethostbyaddr() - IP para nome
socket.gethostname() - Retorna o nome do computador local
socket.getservbyport() - Retorna nome de serviço
socket.getservbyname() - Retorna porta do serviço

'''