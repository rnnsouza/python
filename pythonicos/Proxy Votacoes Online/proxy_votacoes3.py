# -*- coding: utf-8 -*-

# Como funciona as burlações de votações online. Parte 2
# Material abaixo absorvido do curso Pythonicos, para estudos e conheicmento

import requests 

def proxy():
	url = "http://gimmeproxy.com/api/getProxy?protocol=http"
	r = requests.get(url).json()
	return {r['protocol']:r['curl']}


url = "http://www.ferendum.com/pt/votarpost2.php"

proxies = proxy()	

# Edit and Resend, Request Body (pega o que foi enviado)
# Substitui & por ,  e =  por :
# Ficando na estrutura do dicionário
data = {"record1":"","record2":"","pregunta_ID":"45561","sec_digit":"91791","config_anonimo":"1","config_aut_req":"0","titulo":"Votaria+em+Jair+messias+bolsonaro"}

try:
	r = requests.post(url,data=data,proxies=proxies)
	print(r.status_code)
	if "Obrigado por participar desta enquete" in r.content.decode():
		print("Voto Realizado com Sucesso!")
except:
	print("Error!")