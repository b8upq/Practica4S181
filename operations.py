#### IMPORTACION DE LIBRERIAS #####
import sqlite3


conexion = sqlite3.connect('Almacen_Bebidas.db')


####### DECLARACION DE VARIABLES #######
class Almacen:
    
    def altaBD(self, nombre, clasificacion, marca, precio):
        id = int(input("Ingresa el ID de tu bebida: "))
        nombre = str(input("Ingresa el nombre de la bebida: "))
        clasificacion = str(input("Ingresa la clasificación de la bebida: "))
        marca = str(input("Ingresa la marca de la bebida: "))
        precio = float(input("Ingresa el precio de tus bebida: "))