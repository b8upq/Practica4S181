from operations import *

drinks = Almacen()

class Menu:
    def opcion1():
        idR = int(input("Ingresa el ID de tu bebida: "))
        nombreR = str(input("Ingresa el nombre de la bebida: "))
        clasificacionR = str(input("Ingresa la clasificación de la bebida: "))
        marcaR = str(input("Ingresa la marca de la bebida: "))
        precioR = float(input("Ingresa el precio de tus bebida: "))

        drinks.altaBD(idR,nombreR,clasificacionR,marcaR,precioR)
        
    def opcion2():
        print("Has escogido la opción 2.")    

    def opcion3():
        print("Selecciona que campo deseas consultar: ")
        print("1. ID, 2.NOMBRE, 3. CLASIFICACIÓN, 4. MARCA, 5. PRECIO, 6. Escribe '0' para salir")
        def search1():
            sID = int(input("Ingresa el id:"))
            drinks.searchID(sID)
        
        def search2():
            searchnombre = str(input("Ingresa el nombre:"))
            drinks.searchNOMBRE(searchnombre)

        def search3():
            searchCLAS = str(input("Ingresa el clasificación:"))
            drinks.searchCLAS(searchCLAS)
            
        def search4():
            searchMARCA = str(input("Ingresa el marca:"))
            drinks.searchMARCA(searchMARCA)
            
        def search5():
            searchPRECIO = float(input("Ingresa el precio:"))
            drinks.searchPRECIO(searchPRECIO)
            
        opciones = {
            1: search1,
            2: search2,
            3: search3,
            4: search4,
            5: search5
        }
        
        while True:
            seleccion = int(input("Elige una opción de consulta: "))
            if seleccion == 0:
                    print("SALIENDO DEL MENU DE CONSULTAS....")
                    print("-----Estas de nuevo en el menú principal.-----")
                    break
            if seleccion in opciones:
                opciones[seleccion]()   
            else:
                print("Opción inválida. Por favor, elige nuevamente.")
        
    def opcion4():
        print("Selecciona que campo deseas actualizar: ")
        print("1.NOMBRE, 2. CLASIFICACIÓN, 3. MARCA, 4. PRECIO, 5. Escribe '0' para salir")
        def update1():
            uID = int(input("Ingresa el id:"))
            unombre = str(input("Ingresa el nombre:"))
            drinks.updateNOMBRE(uID,unombre)
        
        def update2():
            uID = int(input("Ingresa el id:"))
            uCLAS = str(input("Ingresa el clasificación:"))
            drinks.updateCLAS(uID,uCLAS)

        def update3():
            uID = int(input("Ingresa el id:"))
            uMARCA = str(input("Ingresa el marca:"))
            drinks.updateMARCA(uID,uMARCA)
            
        def update4():
            uID = int(input("Ingresa el id:"))
            uPRECIO = float(input("Ingresa el precio:"))
            drinks.updatePRECIO(uID,uPRECIO)
        
            
        opciones = {
            1: update1,
            2: update2,
            3: update3,
            4: update4
        }
        
        while True:
            seleccion = int(input("Elige una opción de actualización: "))
            if seleccion == 0:
                    print("\nSALIENDO DEL MENU DE ACTUALIZACIÓN....")
                    print("\n-----Estas de nuevo en el menú principal.-----")
                    break
            if seleccion in opciones:
                opciones[seleccion]()   
            else:
                print("Opción inválida. Por favor, elige nuevamente.")  
    
    
print("------ MENU ------")
print("1. Genera un registro.")
print("2. Elimina un registro.")
print("3. Realiza una consulta.")
print("4. Realiza una actualización de datos.")
print("0. Salir")

opciones = {
    1: Menu.opcion1,
    2: Menu.opcion2,
    3: Menu.opcion3,
    4: Menu.opcion4
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