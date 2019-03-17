# -*- coding: utf-8 -*-

# media, mediana, moda

def media(list):
	#x = 0
	#n = 0
	#for i in list:
		#x += i
		#n += 1
	#return x/n
	 return sum(list)/float(len(list))

def mediana(list):
	lista_ordenada = sorted(list)
	t = len(lista_ordenada)

	if t % 2 == 0:
		mediana = (lista_ordenada[int(t/2)] + lista_ordenada[int((t/2) +1)])/2
	elif t % 2 == 1:
		mediana = lista_ordenada[int(t/2)]

	return mediana

def moda (list):
	lista_dic = {} #dicionário, é um objeto que recebe uma chave e um valor

	for l in list:
		if l not in lista_dic:
			lista_dic[l] = 1
		else:
			lista_dic[l] +=1

	maior_repeticao = max(lista_dic.values()) #pega maior elemento da lista. .values pega todos os valores da lista

	for i in lista_dic:
		if lista_dic[i] == maior_repeticao:
			moda = i

	return moda
