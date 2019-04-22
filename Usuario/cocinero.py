from usuario import Usuario

class Cocinero(Usuario):
    def __init__(self, especialidad, identificadorCo, nombreCo, apellidoCo, emailCo, telefonoCo, dniCo):
        super().__init__(identificadorCo, nombreCo, apellidoCo, emailCo, telefonoCo, dniCo)
        self.especialidad = especialidad
        self.cocinando = False
    
    def cocinar(self):
        self.cocinando = True
    
    def informacion(self):
        print(self.especialidad, self.identificador, self.nombre, self.apellido, self.email, self.telefono, self.dni)
