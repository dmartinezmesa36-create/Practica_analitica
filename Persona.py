from typing import List

class Persona:
    def __init__(self, nombre, apellido, ciudad, edad, correo, documento):
        self.nombre = nombre
        self.apellido = apellido
        self.ciudad = ciudad
        self.edad = edad
        self.correo = correo
        self.documento = documento


# --- Funciones del menú ---

def agregar_persona(personas: List[Persona]):
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    ciudad = input("Ciudad: ")
    
    edad = int(input("Edad: "))
    while True:
        if edad < 0 or edad >= 120:
            print("La edad no puede ser negativa ni mayor a 120")
            return
        else:
            print("Edad válida")
            break

    correo = input("Correo: ")
    while True:
        if "@" in correo and "." in correo:
            print("Correo válido")
            break
        else:
            print("Correo inválido, ingrese nuevamente")
            correo = input("Correo: ")

    documento = int(input("Documento: "))
    if documento % 2 == 0:
        print("El documento debe ser impar")
        return

    nueva = Persona(nombre, apellido, ciudad, edad, correo, documento)
    personas.append(nueva)
    print("Persona agregada correctamente")


def listar_personas(personas: List[Persona]):
    if not personas:
        print("No hay personas registradas")
    else:
        for p in personas:
            print(p.nombre, p.apellido, p.edad, p.ciudad, p.correo, p.documento)


def buscar_persona(personas: List[Persona]):
    if not personas:
        print("No hay personas registradas")
        return
    
    doc = int(input("Ingrese el documento a buscar: "))

    for p in personas:
        if p.documento == doc:
            print("\n--- Persona encontrada ---")
            print(p.nombre, p.apellido, p.edad, p.ciudad, p.correo, p.documento)
            return
    
    print("No se encontró ninguna persona con ese documento.")


def eliminar_persona(personas: List[Persona]):
    if not personas:
        print("No hay personas registradas")
        return

    doc = int(input("Ingrese el documento de la persona a eliminar: "))

    for i, p in enumerate(personas):
        if p.documento == doc:
            print(f"Persona {p.nombre} {p.apellido} eliminada correctamente.")
            del personas[i]
            return

    print("No se encontró una persona con ese documento.")


# --- NUEVA FUNCIÓN MODIFICAR PERSONA ---

def modificar_persona(personas: List[Persona]):
    if not personas:
        print("No hay personas registradas")
        return

    doc = int(input("Ingrese el documento de la persona a modificar: "))

    for p in personas:
        if p.documento == doc:
            print("\n--- Persona encontrada ---")
            print("Seleccione qué desea modificar:")
            print("1. Nombre")
            print("2. Apellido")
            print("3. Ciudad")
            print("4. Edad")
            print("5. Correo")
            print("6. Cancelar")

            opcion = input("Opción: ")

            if opcion == "1":
                p.nombre = input("Nuevo nombre: ")
            elif opcion == "2":
                p.apellido = input("Nuevo apellido: ")
            elif opcion == "3":
                p.ciudad = input("Nueva ciudad: ")
            elif opcion == "4":
                nueva_edad = int(input("Nueva edad: "))
                if nueva_edad <= 0 or nueva_edad >= 120:
                    print("Edad inválida")
                    return
                p.edad = nueva_edad
            elif opcion == "5":
                nuevo_correo = input("Nuevo correo: ")
                if "@" not in nuevo_correo or "." not in nuevo_correo:
                    print("Correo inválido")
                    return
                p.correo = nuevo_correo
            elif opcion == "6":
                print("Modificación cancelada.")
                return
            else:
                print("Opción inválida")
                return

            print("Persona modificada correctamente.")
            return

    print("No se encontró una persona con ese documento.")







