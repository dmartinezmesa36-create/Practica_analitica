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
        if edad < 0 and edad >= 120:
            print("La edad no puede ser negativa ")
            return
        else:
            print("Edad válida ")
            break
    correo = input("Correo: ")
    while True:
        if "@" in correo and "." in correo:
            print("Correo válido ")
            break
        else:
            print("Correo inválido , ingrese nuevamente")
            correo = input("Correo: ")
    documento = int(input("Documento: "))
    if documento % 2 == 0: 
        print("El documento debe ser impar ")
        return


    nueva = Persona(nombre, apellido, ciudad, edad, correo, documento)
    personas.append(nueva)
    print("Persona agregada correctamente ")

def listar_personas(personas: List[Persona]):
    if not personas:
        print("No hay personas registradas ")
    else:
        for p in personas:
            print(p.nombre, p.apellido, p.edad, p.ciudad, p.correo)





