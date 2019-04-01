# -*- coding: utf-8 -*-

# Módulo os
import os

# listar o diretório atual, os.getcwd()
print(os.getcwd())

# alterar de diretório, os.chdir()
# criar uma pasta dentro do diretório, os.makedirs()
# os.makedirs('newDir')


# listagem de diretórios
actual_dir = os.getcwd()

def listagem():
	print("Actual dir: "+actual_dir + "\n" + "Content: ")
	for file in os.listdir(actual_dir):
		print(file)
	print("\n")

listagem()

# listando arquivos do diretório anterior
actual_dir = os.path.dirname(actual_dir)
listagem()


# Diretórios

"""
 os.path.abspath() - Retorna path absoluto.
 os.path.isabs() - Retorna True se o path for absoluto.
 os.path.relpath() - Retorna path relativo dado um inicio.
 os.path.dirname() - Retorna string com tudo antes da última barra.
 os.path.basename() - Retorna string com tudo depois da última barra.
 os.path.split() - Tupla com dirname e basename.
 os.path.sep() - Remove as barras.
 os.path.getsize() - Retorna tamanho do path em bytes.
 os.listdir() - Retorna uma lista de string com o nome de arquivos e pastas.
 os.path.exists() - Retorna True se o arquivo ou pasta existir.
 os.path.isdir() - Retorna True se o path for referente a um diretório.
 os.path.isfile() - Retorna True se o path for referente a um arquivo.

"""