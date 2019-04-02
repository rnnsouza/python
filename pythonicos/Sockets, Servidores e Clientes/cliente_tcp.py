# -*- coding:utf-8 -*-

import socket

ip = "127.0.0.1"	# Endereço ip do Servidor
porta = 2222			# Porta que o Servidor está

# Criando o socket
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tupla de destino
dest = (ip, porta) # Tupla de destino

# Fazendo conexão
tcp.connect(dest)

# Ao conectar no Serviço, ele tem um Banner/Mensagem
# Recebe o Banner do Serviço
print(tcp.recv(1024))

while True:
	msg = input(">>>")
	tcp.send(msg)

tcp.close()