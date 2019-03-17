# -*- coding: utf-8 -*-

# método select sort
lista = [3,2,1,54,32,89,231,543]


for i in range(len(lista)):
	menor = i
	for j in range(i+1, len(lista)):
		if lista[j] < lista[menor]:
			menor = j
	if lista[i] != lista[menor]:
		aux = lista[i]
		lista[i] = lista[menor]
		lista[menor] = aux

print(lista)