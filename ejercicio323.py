""" 
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese 
número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello. 

Fruta	Precio
Plátano	1.35
Manzana	0.80
Pera	0.85
Naranja	0.70
"""

precios: dict[str, float] =   {
            "Plátano"   : 1.35,
            "Manzana"   : 0.80,
            "Pera"      : 0.85,
            "Naranja"   : 0.70
            }

def precio_fruta(fruta: str)-> float: 
    return precios.get(fruta, 0)

def precio_total(cantidad: float, precio: float) -> float: 
    return cantidad * precio

if __name__ == "__main__":
    print(
        "FRUTERIA ALBERTO\n"
        "Los Plátanos cuestan 1.35/kg\n"
        "Las Manzanas cuestan 0.80\n"
        "Las Peras cuestan 0.85\n"
        "Las Naranjas cuestan 0.70\n"
        "Si desea salir escriba 'Salir'"
    )
    boton: bool = True
    while boton == True:
        fruta = input("¿Que fruta desea comprar? ").capitalize()
        if fruta not in precios.keys():
            print(f"no tenemos {fruta} en stock")
            continue
        while boton == True:
            try:
                kg = float(input("¿Cuantos kilos desea comprar? "))
            except ValueError:
                print("Los kilos deben ser un numero")
                continue
            print(f"{kg} kilos de {fruta} cuesta {precio_total(kg, precio_fruta(fruta))}")
            boton = False
    
