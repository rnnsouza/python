# -*- coding: utf-8 -*-

# Portscan TCP

from scapy.all import *

for port in range(1,1025):
	resp = sr1(IP(dst='192.168.0.1')/TCP(dport=port,flags='S').verbose=0) # verbose=0, menos informação do resultado do envio do pacote

	# vendo o pacote inteiro
	# print(resp.show())

	# ver extamente qual o valor
	result = resp['TCP'].flags
	if result == 18:
		print("Porta %d abert" %port)
	else:
		print("Porta %d fechada" %port)