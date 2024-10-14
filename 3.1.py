brutoHoras = float(input("introduzca horas: "))
brutoTarifas = float(input("introduzca su tarifa: "))
salario = brutoHoras * brutoTarifas


if brutoHoras > 40.0: 
    salario += (brutoHoras - 40) * (brutoTarifas * 0.5)

print("salario=", round(salario, 2))