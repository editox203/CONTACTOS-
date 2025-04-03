#INICIALIZACION DE AGENDA VACIA

agenda_telefonica = {}

#Funcion para agregar un contacto

def agregar_contacto(nombre, telefono):
    agenda_telefonica[nombre]= telefono
    print(f"contacto {nombre} agregado con exito .")  
       
    #funcion buscar contacto

def buscar_contacto(nombre):
        if nombre in agenda_telefonica:
            print(f"Nombre : {nombre}, Telefono : {agenda_telefonica[nombre]}")
        else:
            print(f"El contacto {nombre} no existe en la agenda.")
            
            
#funcion mostrar los contactos

def mostrar_contactos():
    if agenda_telefonica:
        print("Lista de contactos: ")
        for nombre, telefono in agenda_telefonica.items():
            print(f"Nombre: {nombre}, Telefono: {telefono}")    

    else:
        print("La agenda esta vacia.")
        
#funcion eliminar contacto
def Eliminar_contacto(nombre):
    if nombre in agenda_telefonica:
        del agenda_telefonica[nombre]
        print(f"Contacto {nombre}, {telefono}, !Eliminado con exito!.")
        
    else:
        print(f"El contacto {nombre}, no existe en la agenda.")
        
#loop principal de interaccion 

while True:
    print("\nAgenda Telefonica")
    print("1. Agregar contacto")
    print("2. Buscar contacto") 
    print("3. Mostrar contactos")
    print("4. Eliminar contacto")
    print("5. Salir")
    
    opcion = input("Seleccione una opcion: ")
    
    if opcion== "1":
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el telefono del contacto: ")
        agregar_contacto(nombre, telefono)
        
    elif opcion == "2":
        nombre = input("Ingrese el nombre del contacto a buscar: ")
        buscar_contacto(nombre)
        
    elif opcion == "3":
        mostrar_contactos()
    
    elif opcion == "4":
        nombre = input(" ingrese el nombre del contacto a eliminar: ")
        Eliminar_contacto(nombre)
        
    elif opcion == "5":
        print("Saliendo de la agenda telefonica.")
        break
    
    else: 
        print("Opcion invalida. Por favor seleccione una opcion valida.")