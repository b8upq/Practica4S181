#### IMPORTACION DE LIBRERIAS #####
import sqlite3




####### DECLARACION DE VARIABLES #######
class Almacen:
    
    def self(self, id, nombre, clasificacion, marca, precio):
        self.id = id
        self.nombre = nombre
        self.clasificaciom = clasificacion
        self.marca = marca
        self.precio = precio
    
    def altaBD(self, id, nombre, clasificacion, marca, precio):
        conexion = sqlite3.connect('Almacen_Bebidas.db')
        cursor = conexion.cursor()
        instruccion = f"INSERT INTO Bebidas VALUES ({id}, '{nombre}', '{clasificacion}', '{marca}', {precio})"
        cursor.execute(instruccion)
        conexion.commit()
        conexion.close()
        print("¡Registro exitoso!")

        