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






