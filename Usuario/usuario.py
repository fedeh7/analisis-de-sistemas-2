class Usuario():

    def __init__(self, identificador, nombre, apellido, email, telefono, dni):
        self.identificador = identificador
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.dni = dni
    
    def informacion(self):
        print(self.identificador, self.nombre, self.apellido, self.email, self.telefono, self.dni)





