class Persona:

    
    def __init__(self,nombre,apellido,ciudad,edad,correo):
        self.nombre=nombre
        self.apellido=apellido
        self.ciudad=ciudad
        self.edad=edad
        self.correo=correo
        pass

    lista_nombres = []
    lista_apellidos = []
    lista_cidad = []
    lista_edad = []
    lista_correo = []

    def agregar_nombre(self):
        Persona.lista_nombres.append(self.nombre)
        print(f"{self.nombre} agregado correctamente.")

    def agregar_apellido(self):
        Persona.lista_apellidos.append(self.apellido)
        print(f"{self.apellido} agregado correctamente.")
    
    def agregar_ciudad(self):
        Persona.lista_cidad.append(self.ciudad)
        print(f"{self.ciudad} agregado correctamente.")

    def agregar_edad(self):
        Persona.lista_edad.append(self.edad)
        print(f"{self.edad} agregado correctamente.")
    
    def agregar_edad(self):
        Persona.lista_correo.append(self.correo)
        print(f"{self.correo} agregado correctamente.")
    


    



