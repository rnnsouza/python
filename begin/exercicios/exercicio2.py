# -*- coding: utf-8 -*-

#Media

nota1 = float(input("Informe primeira nota: "))
nota2 = float(input("Informe segunda nota: "))

media = (nota1+nota2)/2

print("Média é: %.1f" %(media))

if media >= 6:
	print("Aprovado!")
else:
	print("Reprovado!")