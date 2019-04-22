from usuario import Usuario

class Delivery(Usuario):
    def __init__(self, identificadorD, nombreD, apellidoD, emailD, telefonoD, dniD):
        super().__init__(identificadorD, nombreD, apellidoD, emailD, telefonoD, dniD)
        self.vehiculo_propio = False
        self.repartiendo_pedidos = False

    def tiene_vehiculo(self):
        self.vehiculo_propio = True

    def repartiendo(self):
        self.repartiendo_pedidos = True
