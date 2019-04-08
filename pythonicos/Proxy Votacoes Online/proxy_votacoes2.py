# -*- coding: utf-8 -*-

# Como funciona as burlações de votações online. Parte 2
# Material abaixo absorvido do curso Pythonicos, para estudos e conheicmento

import requests

url = "http://gimmeproxy.com/api/getProxy"
r = requests.get(url).json()
proxy = r['curl']
protocolo = r['protocol']

print({protocolo:proxy})

'''
# url da votação. Pega o endereço a partir do evento click do item selecionado
# url prsente no Headers
url = "http://url...."

# método put() para fazer o voto
r = requests.put(url)

# verifica status, se voltar 204 significa que ele funcionou, mas a resposta foi vazia
print(r.status_code)

# se deu 204 a resposta será vazia
print(r.content)

# Iniciando loop para vários votações
while 1:
	r = requests.put(url)
	if r.status_code == 204:
		print("Voto Realizado com Sucesso!")

'''