# -*- coding: utf-8 -*-
# Exemplo obtido no curso Pythonicos pelo Matheus Bernardes (https://github.com/mthbernardes)

import socket

ip = "127.0.0.1"
porta = 2222

# Criando o Socket
# AF_INET -> Especifica que será usado IPV4
# SOCK_STREAM -> Especifica que será usado protocolo TCP/IP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define porta que será aberta. bind() sempre recebe uma tupla
s.bind((ip, porta))

# Armazena em uma fila antes de receber o accept()
# Fila de espera, máximo de pessoas na fila serão 5
s.listen(5)

# o s.accept() irá retirar a pessoa da fila de espera
while True:
	# conn -> recebe a conexão, onde podemos enviar/receber mensagem
	# addr -> recebe uma tupla contendo o 'IP' e a 'PORTA' de quem está conectando
	conn, addr = s.accept() # Aceita a conexão removendo da lista do listen()
	conn.send("Bem vindo ao seu primeiro servidor TCP\n") # Cliente irá receber essa mensagem
	print("Conexão de  %s:%d" %(addr[0].addr[1])) # Serviço
	conn.send(">>>")
	msg = conn.recv(1024) # Recebendo em até 1024 bytes o que o cliente digitou/respondeu
	print("Mensagem recebida: %s" %msg) # Print na tela do serviço o que foi respondido
	conn.close()
	break

s.close()