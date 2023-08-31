numero1 = int(input('ingrese un valor numerico: '))
numero2 = int(input( 'ingrese un segundo valor numerico: '))
numero3 = int(input('ingrese el tercer valor numerico: '))

if numero1 != numero2 and numero2 != numero3 and numero3 != numero1:
    if numero1 > numero2 and numero1 > numero3: 
     print('el numero mayor es : ', numero1)
    elif numero2 > numero1 and numero2 > numero3 :
     print('el numero mayor es : ', numero2)
    else:
     print('el numero mayor es : ', numero3)
else:
    print('alguno de los valores ingresados son iguales ')

