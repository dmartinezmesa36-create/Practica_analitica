from Persona import Persona

from typing import List


from Persona import Persona

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Agregar persona")
    print("2. Mostrar nombres")
    print("3. Mostrar apellidos")
    print("4. Salir")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        cidad = input("ingrese la ciudad")
        edad = input("ingrese la edad")
        correo = input("ingrese el correo")
        Persona(nombre, apellido,cidad,edad,correo)   # 

    elif opcion == "2":
        Persona.mostrar_nombres()

    elif opcion == "3":
        Persona.mostrar_apellidos()

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida, intente de nuevo.")
mostrar_menu()



