# -*- coding: utf-8 -*-

# dicionários, trabalham com índice:valor
# não são ordenados, pois trabalham com o valor
# var = dict()
# var = {}

var = {'ip':'192.168.0.1','port':80}
print(var['ip'])  							# '192.168.0.1'
print(var['port']) 							#  80

print('%s:%d' %(var['ip'],var['port'])) 	#192.168.0.1:80


# Alterando valores dentro do dicionário
var['ip'] = '200.204.110.89'
print(var)									# {'ip': '200.204.110.89', 'port': 80}

# Inserindo novo registro/elemento no dicionário
var['service'] = 'http'
print(var)									# {'ip': '200.204.110.89', 'port': 80, 'service': 'http'}

# Removendo elemento do dicionário
del var['service']
print(var)									# {'ip': '200.204.110.89', 'port': 80}

# Adicionando novamente
var['service'] = 'http'


# FUNÇÕES
# keys(), values() e items()

# Retornando uma lista contendo as CHAVES do dicionário, função keys()
print(var.keys())							# dict_keys(['ip', 'port', 'service'])

# Retornando uma lista contendo os VALORES do dicionário, função values()
print(var.values())							# dict_values(['200.204.110.89', 80, 'http'])

# Retornando uma lista contendo uma tupla com os elementos do dicionário, função items()
print(var.items())							# dict_items([('ip', '200.204.110.89'), ('port', 80), ('service', 'http')])

# Acessando a lista no índice 1
print(list(var)[1])

for key,values in var.items():
	print(key + ':', values)				# ip: 200.204.110.89
											# port: 80
											# service: http

# Verificar se tem um índice dentro do dicionário
print('ip' in var)							# True
print('ip' not in var)						# False


# Verificando se tem um índice dentro do dicionário, com métdo get()
# Diferenças entre o get() e o in, o get permite retornar um valor quando não encontra

print(var.get('host','not founded'))		# not founded
print(var.get('ip','not founded'))			# 200.204.110.89


# Define um default para um índice do dicionário, função setdefault(). system será sempre thanos
print(var)									# {'ip': '200.204.110.89', 'port': 80, 'service': 'http'}

print(var.setdefault('system','thanos'))	# thanos
print(var)									# {'ip': '200.204.110.89', 'port': 80, 'service': 'http', 'system': 'thanos'}