archivo = input("nombre del archivo:")
text = open(archivo, "r")
for linea in text:
    print(linea)

