# -*- coding: utf-8 -*-

import zipfile as zip
import os

zipado = zip.ZipFile("dumpFile.zip")

# retornando uma lista com todos os arquivos dentro de 'dumpFile.zip'
print(zipado.namelist())

for file in zipado.namelist():
	print(file)

# pegando informações dentro do arquivo zipado
info = zipado.getinfo("dumpFile/teste.txt")
# dir(info)
print(dir(info))

# vendo tamanho do arquivo
print(info.file_size)

# vendo tamanho do arquivo comprimido
print(info.compress_size)



### EXTRAINDO ARQUIVOS ###

print(zipado.extract('dumpFile/teste.txt'))

print(os.listdir('dumpFile'))

# zipado.close()

### CRIANDO ARQUIVO ZIP E ADICIONANDO CONTEÚDO

zipback = zip.ZipFile('arquivoZipado.zip','w')
zipback.write('dumpFile.zip')
zipback.close()

zipado.close()