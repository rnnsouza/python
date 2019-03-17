# -*- coding: utf-8 -*-

import sys

num1 = int(input("Digite o primeiro número: "))
operador = input("Digita o operador: ")
num2 = int(input("Digite o segundo número: "))

#tam = len(operador)
if operador != "-" and operador != "+" and operador != "/" and operador != "*" and operador != "%" and operador != "**":
	print("Operador inválido!")
	sys.exit()

# soma +
if operador == "+":
	resultado = num1 + num2
# subtração -
elif operador == "-":
	resultado = num1 - num2
# divisão /
elif operador == "/":
	resultado = num1 / num2
# multiplicação
elif operador == "*":
	resultado = num1 * num2
# modulo
elif operador == "%":
	resultado = num1 % num2
# expoente
elif operador == "**":
	resultado = num1**num2
else:
	print("Operador inválido!")

print(resultado)