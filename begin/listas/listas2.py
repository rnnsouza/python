lista1 = [1,2,3,4,5]
lista2 = ["ola","mundo","!"]
lista3 = [0,"ola","biscoito","bolacha",9.99,True]

for i in lista3:
	print(i)

# print 0 to 9
for i in range(10):
	print(i)

# print 10 to 19
for i in range(10,20):
	print(i)

# print 10 to 19 (two in two)
for i in range(10,20,2):
	print(i)


# Referênciando uma lista

var = [1,2,3,4,5,6,7]
# nesse momento, var1 está referenciando a lista var, mas não está criando outra lista
var1 = var

# "ola mundo" será colocado na lista var, que também aparecerá na var1
var.append("ola mundo") 