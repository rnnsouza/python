# -*- coding: utf-8 -*-

# pip install lxml
# Material abaixo absorvido do curso Pythonicos, para estudos e conheicmento

import requests
from lxml import html

r = requests.get("http://empregacampinas.com.br/2019/04/redes-senior-pleno-campinas-sp-1-vagas/")

# xpath, linguagem para correr dentro de arquivos xml, html
# [0].strip(), primeiro elemento, e strip() para retirar espaços a direita e a esquerda
tree = html.fromstring(r.content)
print(tree.xpath("/html/body/div[1]/article/div/div[2]/div/h1/span/text()")[0].strip()) # text(), retorna o texto que está dentro daquele elemento
print(tree.xpath("/html/body/div[1]/article/div/div[2]/div/p[5]/strong/text()")[0].strip())
print(tree.xpath("/html/body/div[1]/article/div/div[2]/div/p[10]/a[2]/text()")[0].strip()) # para trazer o atributo de a[2], ao invés de text(), colocaria @href