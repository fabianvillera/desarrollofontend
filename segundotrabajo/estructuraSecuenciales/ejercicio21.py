# -*- coding: utf-8 -*-
import math
lado1 = float(input('ingrese el primer lado de el triangulo : '))
lado2 = float(input('ingrese el primer lado de el triangulo : '))
lado3 = float(input('ingrese el primer lado de el triangulo :'))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2  and lado2 + lado3 > lado1:

  semiPerimetro = (lado1 + lado2 + lado3 ) / 2
  perimetro = lado1 + lado2 + lado3
  areaTriangulo = math.sqrt(semiPerimetro * (semiPerimetro - lado1) * (semiPerimetro - lado2) * (semiPerimetro - lado3))

  print('El semiperímetro del triángulo formado por las coordenadas dadas es', semiPerimetro)
  print('El área del triángulo es:', areaTriangulo)
  print('El perímetro del triángulo es:', perimetro)
  print( 'el triangulo existe ')
else:
  print("los puntos dados no forman un triangulo.")
  print (' no  existen los parametros anteriores para estas cordenadas')

