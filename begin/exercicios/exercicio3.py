# -*- coding: utf-8 -*-
# Equação de 2 grau
from math import sqrt

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = b**2 - 4*a*c
raiz_delta = sqrt(delta)

x1 = (-b + raiz_delta)/(2*a)
x2 = (-b - raiz_delta)/(2*a)

print("x1 = %.1f"%(x1))
print("x2 = %.1f"%(x2))