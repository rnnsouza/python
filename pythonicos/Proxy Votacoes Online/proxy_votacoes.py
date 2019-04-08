# -*- coding: utf-8 -*-

# Como funciona as burlações de votações online
# Material abaixo absorvido do curso Pythonicos, para estudos e conheicmento

import requests
import random
from pprint import pprint

def proxies(q,mode='json'):
	url = "http://proxy.tekbreak.com/%s/%s" %(q,mode)
	r = requests.get(url)

	# Escolho 1 dos n proxies. Passando o tamanho da minha lista no retorn r.json()
	x = random.randrange(0,len(r.json()))

	proxy = "%s://%s/%s" %(r.json()[x]["type"].lower(),r.json()[x]["ip"],r.json()[x]["port"])
	proxies = {r.json()[x]["type"].lower():proxy}
	return proxies

proxies = proxies(q=100)
# Passa um dicionário para o requests
r = requests.get("http://ipinfo.io",proxies=proxies)
pprint(r.content)