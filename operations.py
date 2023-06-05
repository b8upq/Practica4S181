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
  
    def deleteID(self, id):
        conexion = sqlite3.connect('Almacen_Bebidas.db')
        cursor = conexion.cursor()
        instruccion = f"DELETE FROM Bebidas WHERE id = {id}"
        cursor.execute(instruccion)
        conexion.commit()
        conexion.close()
        print("¡Se elimino correctamente!")
        
    def searchID(self, id):
        conexion = sqlite3.connect('Almacen_Bebidas.db')
        cursor = conexion.cursor()
        instruccion = f"SELECT * FROM Bebidas WHERE id = {id}"
        cursor.execute(instruccion)
        datos = cursor.fetchall()
        conexion.commit()
        conexion.close()
        
        if (datos == []):
            print("No existen articulos con ese ID.")  
        else:
            print(datos)
        
    def searchNOMBRE(self, nombre):
        conexion = sqlite3.connect('Almacen_Bebidas.db')
        cursor = conexion.cursor()
        instruccion = f"SELECT * FROM Bebidas WHERE nombre like '{nombre}%'"
        cursor.execute(instruccion)
        datos = cursor.fetchall()
        conexion.commit()
        conexion.close()
        
        if (datos == []):
            print("No existen articulos con ese nombre.")  
        else:
            print(datos)
        
    def searchCLAS(self, clasificacion):
        conexion = sqlite3.connect('Almacen_Bebidas.db')
        cursor = conexion.cursor()
        instruccion = f"SELECT * FROM Bebidas WHERE clasificacion like '{clasificacion}%'"
        cursor.execute(instruccion)
        datos = cursor.fetchall()
        conexion.commit()
        conexion.close()
        
        if (datos == []):
            print("No existen articulos con ese clasificación.")  
        else:
            print(datos)
        
    def searchMARCA(self, marca):
        conexion = sqlite3.connect('Almacen_Bebidas.db')
        cursor = conexion.cursor()
        instruccion = f"SELECT * FROM Bebidas WHERE marca like '{marca}'"
        cursor.execute(instruccion)
        datos = cursor.fetchall()
        conexion.commit()
        conexion.close()
        
        if (datos == []):
            print("No existen articulos con ese marca.")  
        else:
            print(datos)
        
    def searchPRECIO(self, precio):
        conexion = sqlite3.connect('Almacen_Bebidas.db')
        cursor = conexion.cursor()
        instruccion = f"SELECT * FROM Bebidas WHERE precio = {precio}"
        cursor.execute(instruccion)
        datos = cursor.fetchall()
        conexion.commit()
        conexion.close()
        
        if (datos == []):
            print("No existen articulos con ese precio.")  
        else:
            print(datos)

    def updateNOMBRE(self, id, nombre):
            conexion = sqlite3.connect('Almacen_Bebidas.db')
            cursor = conexion.cursor()
            instruccion = f"UPDATE Bebidas SET nombre = '{nombre}' WHERE id = {id}"
            cursor.execute(instruccion)
            conexion.commit()
            conexion.close()        
            print("Se ha actualizado el nombre correctamente.")
            
    def updateCLAS(self, id, clasificacion):
            conexion = sqlite3.connect('Almacen_Bebidas.db')
            cursor = conexion.cursor()
            instruccion = f"UPDATE Bebidas SET clasificacion = '{clasificacion}' WHERE id = {id}"
            cursor.execute(instruccion)
            conexion.commit()
            conexion.close()        
            print("Se ha actualizado el clasificación correctamente.")
            
    def updateMARCA(self, id, marca):
            conexion = sqlite3.connect('Almacen_Bebidas.db')
            cursor = conexion.cursor()
            instruccion = f"UPDATE Bebidas SET marca = '{marca}' WHERE id = {id}"
            cursor.execute(instruccion)
            conexion.commit()
            conexion.close()        
            print("Se ha actualizado el marca correctamente.")
            
    def updatePRECIO(self, id, precio):
            conexion = sqlite3.connect('Almacen_Bebidas.db')
            cursor = conexion.cursor()
            instruccion = f"UPDATE Bebidas SET precio = {precio} WHERE id = {id}"
            cursor.execute(instruccion)
            conexion.commit()
            conexion.close()        
            print("Se ha actualizado el precio correctamente.")
            
    def mostrarTODO(self):
        conexion = sqlite3.connect('Almacen_Bebidas.db')
        cursor = conexion.cursor()
        instruccion = f"SELECT * FROM Bebidas"
        cursor.execute(instruccion)
        datos = cursor.fetchall()
        conexion.commit()
        conexion.close()
        print(datos)

    def mostrarPROMEDIO(self):
        conexion = sqlite3.connect('Almacen_Bebidas.db')
        cursor = conexion.cursor()
        instruccion = f"SELECT AVG(precio) FROM Bebidas"
        cursor.execute(instruccion)
        datos = cursor.fetchall()
        conexion.commit()
        conexion.close()
        print("El promedio es: ",datos)
        
    def contarBebidas(self, marca):
        conexion = sqlite3.connect('Almacen_Bebidas.db')
        cursor = conexion.cursor()
        instruccion = f"SELECT COUNT(*) FROM Bebidas WHERE marca like '{marca}%'"
        cursor.execute(instruccion)
        datos = cursor.fetchall()
        conexion.commit()
        conexion.close()
        
        if (datos == [(0,)]):
            print("No existen articulos con ese nombre.")  
        else:
            print("La cantidad de bebidas de la marca es: ",datos)
        
    def contarClas(self, clasificacion):
        conexion = sqlite3.connect('Almacen_Bebidas.db')
        cursor = conexion.cursor()
        instruccion = f"SELECT COUNT(*) FROM Bebidas WHERE clasificacion like '{clasificacion}'"
        cursor.execute(instruccion)
        datos = cursor.fetchall()
        conexion.commit()
        conexion.close()
        
        if (datos == [(0,)]):
            print("No existen articulos con ese nombre.")  
        else:
            print("La cantidad de clasificación es: ",datos)