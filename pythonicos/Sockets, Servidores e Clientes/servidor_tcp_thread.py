# -*- coding: utf-8 -*-

import socket
from threading import Thread 	# Um serviço vai trabalhar com várias instâncias
								# Recebe uma conexão e fica disponível para receber outra conexão

def agent(conn):
	while True:
		msg = conn.recv(1024)
		if not msg:
			break
		print("Mensagem recebida: %s" %msg)
	conn.close()


ip = "127.0.0.1"
porta = 2222

# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define porta que vai ser aberta
s.bind((ip, porta))

# Armazena em uma fila antes de receber o accept()
s.listen(5)

while True:
	conn, addr = s.accept() # Aceita conexão removendo da lista do listen()
	conn.send("Seja muito bem vindo ao meu primeiro servidor!\n")
	print("Conexão de %s:%d" %(addr[0], addr[1]))
	t = Thread(target=agent, arg=(conn,))
	t.start()

s.close()