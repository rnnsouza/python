# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=n2UV56gBk9U
# pip install requests
import requests

r = requests.get("http://pythonicos.com.br")
# Retorna status do response do http, 200 (conexão com sucesso)
r.status_code
# Retorna código fonte da página
print(r.content)

# Trabalhando com post, passo para ele quais serão meus argumentos
# r = requests.post("http://pythonicos.com.br/post",data={'key':'value'})

'''
if "parentNode" in r.content.decode():
	print("OK")
else:
	print("NOT")
'''

payload = {'username':'admin@admin.com.br','password':'admin'}
r = requests.post("http://pythonicos.com.br/login/?next=/",data=payload)
print(r.content)

# Apartir daqui, posso começar a fazer tratativas. Verificar se tal mensagem está no retorn
# "mensagem" in r.content, e ir tratando elas conforme o objetivo

### PARÂMETROS EM URL	
payload = {'key1':'value1','key2':'value2'}
r = requests.get("http://pythonicos.com.br/get",params=payload)
print(r.url)

### JSON
r = requests.get("http://api.pythonicos.com.br/events")
print(r.json())

# printar as reposta de forma mais legivel, saundo o pprint()
# from pprint import pprint()
# pprint(r.json()[0])


### HEADER CUSTOMIZADO
url = "http://api.pythonicos.com.br/some/endpoint"
headers = {'user-agent':'my-app/0.0.1'}
r = requests.get(url,headers=headers)