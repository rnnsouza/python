# -*- coding: utf-8 -*-

import requests

# Tupla contendo usuario e a senha
r = requests.get("http://192.168.0.1/",auth=('user','password'))

print(r.status_code)
print(r.content)
print(type(r.status_code))


if r.status_code == 200:
	print("Conectado")
else:
	print("Next loop")


