# -*- coding: utf-8 -*-=

# números aleatórios importando modo random
import random

numero = random.randint(0,10)
print(numero)

# método choice escolhe um elemento dentro de uma lista
lista = [1,2,3,4]
numero2 = random.choice(lista)
print("Número %d foi o escolhido" %numero2)