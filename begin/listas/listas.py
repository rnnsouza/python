# -*- coding: utf-8 -*-
#listas
minha_lista = ["abacaxi", "melancia", "abacate"]
minha_lista_2 = [1,2,3,4,5,6,7]
lista_mista = ["abacaxi",1,2,4,1.89,True]
print(minha_lista[1])

#percorrendo minha lista
for item in minha_lista:
	print(item)

#tamanho da lista
tamanho = len(minha_lista)
print(tamanho)

#adicionar novo valor na lista usando append()
minha_lista.append("laranja")

print(minha_lista)

#procurando elemento na lista
x = 7

if x in minha_lista_2:
	print("%d está na minha lista" %x)
else:
	print("%d não está na lista" %x)

#deletando elemento da lista
# deleta da posição 2 até o final
del minha_lista[2:]
print(minha_lista)
# deleta toda a lista
del minha_lista[:]
print(minha_lista)