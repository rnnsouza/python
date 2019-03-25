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


# MÉTODOS

# index()   retorna em qual posição está tal valor, lista.index(1)
# append()  insere elemento no final da lista, lista.append("novo elemento")
# insert()  insere elemento na lista na posição desejada, lista.insert("oi",3) posição 3
# extend()  adiciona elementos de uma lista em outra lista, lista1.extend(lista2) 

# remove()  remove um elemento da lista, lista.remove("elemento") ou del lista
# pop()     remove um elemento dado sua posição, lista.pop(4) indice 4 da lista

# sort()    coloca a lista em ordem alfabética, lista.sort()
# reverse() inverte a lista, lista.reverse()
# count()   dado um elemento conta quantas vezes ele aparece na lista, lista.count("elemento")