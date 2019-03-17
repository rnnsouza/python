# -*- coding: utf-8 -*-

#ordenando listas
lista = [6,4,2,8,76,43,21,98,0,1,22]

# método sort altera uma lista que já existe (crescente). também altera alfabéticamente
lista.sort() # ou lista = sorted(lista) que retorna uma lista ordenada
print(lista)

# ordenando de forma descrescente
lista.sort(reverse=True)
print(lista)

# invertendo a lista. pegando o ultimo e jogando na primeira posição
lista.reverse()
print(lista)