puntuacion = float(input("Introduzca puntuación:"))

if puntuacion >= 0.9 and puntuacion < 10.1:
    print("Sobresaliente")
elif puntuacion < 0.9 and puntuacion >= 0.8:
    print("notable")
elif puntuacion < 0.8 and puntuacion >= 0.7:
    print("bien")
elif puntuacion < 0.7 and puntuacion >= 0.6:
    print("suficiente")
elif puntuacion < 0.6 and puntuacion >= 0:
    print("insuficiente")   
else:
    print("puntuaccion incorrecta")
