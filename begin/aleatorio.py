# -*- coding: utf-8 -*-

import random

def geraListInt(tam):
	lista = []
	for i in range(tam): # retorna uma lista conforme o tamanho tam
		lista.append(random.randint(0,tam))

	return lista

