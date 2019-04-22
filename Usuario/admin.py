from usuario import Usuario

class Admin(Usuario):
    def __init__(self, privilegios, identificadorA, nombreA, apellidoA, emailA, telefonoA, dniA):
        super().__init__(identificadorA, nombreA, apellidoA, emailA, telefonoA, dniA)
        self.privilegios = privilegios
        self.gestionar_ganancias = False
        self.gestionar_gastos = False
        self.gestionar_stock = False
    
    def ganancias(self):
        self.gestionar_ganancias = True
    
    def gastos(self):
        self.gestionar_gastos = True
    
    def stock(self):
        self.gestionar_stock = True