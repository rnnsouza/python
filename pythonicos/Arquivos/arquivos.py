# -*- coding: utf-8 -*-

# Já estando no diretório de uso, caso contrário, colocar o caminho
# Subescrevendo ou criando arquivo

f = open("arquivoTeste.txt",'w')
f.write("Ola mundo!")
f.close()

# Add novos conteúdos
# 'a' -> append
f = open("arquivoTeste.txt",'a')
f.write("\nTudo bem?")
f.close()

# Lendo o arquivo
f = open("arquivoTeste.txt",'r')
read = f.read()	# readlines() transforma tudo em uma lista
print(read)
f.close()