# -*- coding: utf-8 -*-

import socket 

ip = "127.0.0.1"	# Endereço IP do Servidor
porta = 5000 			# Porta que o Servidor está

# Criando instância do socket
# SOCK_DGRAM -> Trabalhando com UDP
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Criando tupla com ip e porta e atribuindo a variável dest
dest = (ip, porta)

while True:
	msg = input(">>>")
	udp.sendto(msg,dest)
	msg, conn = udp.recvfrom(1024)
	print(msg) # Print na mensagem que o Servidor irá retornar

udp.close()