# -*- coding:utf-8 -*-

# Transformar tudo em maiúscula
# --> x.upper()
var = "nOmE"
print(var.upper()) 				# NOME


# Transformar tudo em minúscula
# --> x.lower()
print(var.lower())				# nome


# Dividindo a string e gerando lista
var = "64.242.88.10 - - [07/Mar/2004:16:05:49 -0800] GET /twiki/bin/edit"
# O caractere padrão do split é o espaço ' '
# var = var.split('.')
var = var.split()

print(var[0])

var = "    test		"
var = var.strip() #rstrip(), lstrip()
print(var)

var = "Have a nice day"
var = var.replace("day","week") # replace 'day' by week
print(var)


# UTILIDADES

"""
startswith() - Verifica se a string começa com a string informada
endswith() - Verifica se a string termina com a string informada
join() - Concatena lista
split() - Dividir a string e gerar lista
rtrip() - Remove espaços a direita
lstrip() - Remove espaços a esquerda
strip() - Remove espaços ou string em ambos os lados
replace() - Substitui uma string

"""