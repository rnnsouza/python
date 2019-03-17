# -*- coding: utf-8 -*-

#Verifica se é maior de idade

idade = int(input("Digite sua idade: "))

if idade >= 18:
	print("Maior de idade!")
elif idade > 0 and idade < 18:
	print("Menor de idade!")
else:
	print("Idade inválida!")
	