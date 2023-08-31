# -*- coding: utf-8 -*-
# Solicitar información del empleado
codigoEmpleado = input("Ingrese el código del empleado: ")
nombresEmpleado = input("Ingrese los nombres del empleado: ")
horasTrabajadas = float(input("Ingrese el número de horas trabajadas al mes: "))
valorHora = float(input("Ingrese el valor hora trabajada: "))
retencionFuente = float(input("Ingrese el porcentaje de retención en la fuente: "))

# Calcular salario bruto
salarioBruto = horasTrabajadas * valorHora

# Calcular retención en la fuente
retencion = salarioBruto * (retencionFuente / 100)

# Calcular salario neto
salarioNeto = salarioBruto - retencion

# Mostrar resultados
print("Información del empleado:")
print("Código:", codigoEmpleado)
print("Nombres:", nombresEmpleado)
print("Salario Bruto:", salarioBruto)
print("Retención en la fuente:", retencion)

