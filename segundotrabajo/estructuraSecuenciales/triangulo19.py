# -*- coding: utf-8 -*-

import math

def calcular_altura(ladoTriangulo):
    alturaTriangulo = ladoTriangulo * math.sqrt(3) / 2
    return alturaTriangulo

def calcular_area(ladoTriangulo):
    areaTriangulo = (ladoTriangulo ** 2 * math.sqrt(3)) / 4
    return areaTriangulo

ladoTriangulo = float(input("Ingrese el valor de un lado del triángulo: "))

altura = calcular_altura(ladoTriangulo)
area = calcular_area(ladoTriangulo)
perimetro = ladoTriangulo * 3

print("El perimetro del triangulo es:", perimetro)
print("La altura del triangulo es:", altura)
print("El area del triangulo es:", area)

# segunda solucion 

import math

ladoTriangulo = float(input("Ingrese el valor de un lado del triángulo: "))

alturaTriangulo = ladoTriangulo * math.sqrt(3) / 2
areaTriangulo = (ladoTriangulo ** 2 * math.sqrt(3)) / 4

perimetro = ladoTriangulo * 3

print("El perimetro del triangulo es:", perimetro)
print("La altura del triangulo es:", alturaTriangulo)
print("El area del triangulo es:", areaTriangulo)
