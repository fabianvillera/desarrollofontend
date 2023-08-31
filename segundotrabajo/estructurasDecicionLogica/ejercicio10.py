numeroInscripcion = int(input('ingrese el numero de inscripcion del estudiante : '))
nombreEstudiante = input('ingrese el nombre del estudiante : ')
patrimonio = float ( input('ingrese el parimonio del estudiante : '))
estratoSocial = int(input('ingrese el estudiante al cual pertenece el estudiante '))
VALOR_CONSTANTE = 50000
valorTotal = 0
if patrimonio > 2000000 and estratoSocial > 3:
    valorTotal = VALOR_CONSTANTE + patrimonio * 0.03
    print ('El numero de inscripcion es: ' , numeroInscripcion)
    print ('El nombre del estudiante es : ', nombreEstudiante)
    print ('El valor a pagar por la matricula es: ' , valorTotal)
    print ('El valor total a pagar por el estudiante', nombreEstudiante , 'y numero de inscripcion',numeroInscripcion , 'es:', valorTotal )
else:
    print('el valor total a pagar es : ' , VALOR_CONSTANTE)
    print ('El nombre del estudiante es : ', nombreEstudiante)
    print ('El valor a pagar por la matricula es: ' , valorTotal)
    print ('El valor total a pagar por el estudiante', nombreEstudiante , 'y numero de inscripcion',numeroInscripcion , 'es:', VALOR_CONSTANTE )


