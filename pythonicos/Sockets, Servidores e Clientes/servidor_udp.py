# -*- coding:utf-8 -*-

import socket

ip = "" # omitindo o ip, ele pegará o localhost (127.0.0.1)
porta = 5000

# SOCK_DGRAM -> trabalhando com UDP
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s

# criando a tupla que irá receber o ip, porta
orig = (ip, porta)

# criando o bind
udp.bind(orig)
# s.bind(orig), com with

# Fila de espera, máximo de pessoas na fila serão 5
# udp.listen(5) -> não irá funcionar, por ser UDP. Se outra pessoa tentar conectar, ele irá derrubar uma conexão para iniciar a outra.
# s.liten(5), com with

while True:
	# cliente irá receber uma tupla com o ip e porta
	msg, cliente = recvfrom(1024)
	print(cliente[0], msg)
	if msg:
		try:
			result = socket.gethostbyname(msg.strip())
		except Exception as e:
			result = str(e)
		# manda o result para o cliente que mandou a mensagem	
		udp.sendto(result+'\n', cliente)
		# s.sendto(result+'\n', cliente), com with

udp.close()
# s.close(), com with

# OBS: nc -u 127.0.0.1 5000
# -u por ser UDP