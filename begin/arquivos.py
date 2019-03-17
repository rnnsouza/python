# -*- coding: utf-8 -*-

valor = ""

arq = open("C:\\Users\\DSouza\\Desktop\\arquivo.txt")
#Read all lines into my file, and put in a list.
linhas = arq.readlines()
# Print line by line.
for linha in linhas:
	print(linha)
	valor = linha

#Put all into a only variable.
texto_completo = arq.read()
print(texto_completo)
#Closing file
arq.close()

# Creating a new file from command open mode 'W'
w = open("C:\\Users\\DSouza\\Desktop\\arquivo2.txt","w")
w.write("Meu segundo arquivo")
texto_completo = w.read()
print(texto_completo)