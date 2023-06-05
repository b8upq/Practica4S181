import sqlite3
from operations import *

def opcion1():
    idR = int(input("Ingresa el ID de tu bebida: "))
    nombreR = str(input("Ingresa el nombre de la bebida: "))
    clasificacionR = str(input("Ingresa la clasificación de la bebida: "))
    marcaR = str(input("Ingresa la marca de la bebida: "))
    precioR = float(input("Ingresa el precio de tus bebida: "))

    drinks = Almacen()

    drinks.altaBD(idR,nombreR,clasificacionR,marcaR,precioR)
    
def opcion2():
    print("Has escogido la opción 2.")    

def opcion3():
    print("Has escogido la opción 3.")  
    
def opcion4():
    print("Has escogido la opción 4.")  
    
    
print("------ MENU ------")
print("1. Opción 1")
print("2. Opción 2")
print("3. Opción 3")
print("4. Opción 4")
print("0. Salir")

opciones = {
    1: opcion1,
    2: opcion2,
    3: opcion3,
    4: opcion4
}

while True:
    seleccion = int(input("Elige una opción: "))

    if seleccion == 0:
            print("¡Hasta luego! ¡Vuelva pronto!")
            break
            

    if seleccion in opciones:
        opciones[seleccion]()
        
    else:
        print("Opción inválida. Por favor, elige nuevamente.")