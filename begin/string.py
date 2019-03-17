# -*- coding: utf-8 -*-

a = "Renan"
b = "Fulana"

# concatenar
concatenar = a+" "+b
print(concatenar)

# string lenght
tamanho = len(concatenar)
print(tamanho)

r = 0
for i in concatenar:
	if i != " ":
		continue
	else:
		r+=1

teste = tamanho - r

# number of characters without space
print(teste)

# print the value in the position vector (string)
print(a[2])

# print a part of the string concatenated (start at 0 and end in 7 position)
print(concatenar[0:7])
# start at position 0 until the final
print(concatenar[0:])