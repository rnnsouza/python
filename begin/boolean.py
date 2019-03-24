# -*- coding: utf-8 -*-
divisor = 2

valorDefinido = 7

satisfaction = bool(valorDefinido % divisor == 0)

if satisfaction:
	print("O número é par")
else:
	print("O número é impar")