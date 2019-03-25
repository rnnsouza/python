# -*- coding: utf-8 -*-

divisor = 2

valorDefinido = 7

satisfatorio = bool(valorDefinido % divisor == 0)

if satisfatorio:
	print("O número é par")
else:
	print("O número é impar")