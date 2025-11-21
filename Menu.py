from Persona import (
    Persona,
    agregar_persona,
    listar_personas,
    buscar_persona,
    eliminar_persona,
    modificar_persona
)
from typing import List


def menu():
    personas: List[Persona] = []

    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar persona")
        print("2. Listar personas")
        print("3. Buscar persona")
        print("4. Eliminar persona")
        print("5. Modificar persona")
        print("6. Salir")

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            agregar_persona(personas)
        elif opcion == "2":
            listar_personas(personas)
        elif opcion == "3":
            buscar_persona(personas)
        elif opcion == "4":
            eliminar_persona(personas)
        elif opcion == "5":
            modificar_persona(personas)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida")


menu()

