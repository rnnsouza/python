# -*- coding: utf-8 -*-

# Tuplas são imutáveis

# criar uma tupla
var = ()
# ou var = tuple()

var = (1,2,3,4,5,6,7)

# criando uma tupla com um elemento, coloca uma vírgula no final
var = ("elemento",)

# convertendo tupla para uma lista
var = ("aprendendo", "python", "pythonicos")
print(type(var))

list(var)
print(type(var))

# modo correto
var = list(var)
print(type(var))