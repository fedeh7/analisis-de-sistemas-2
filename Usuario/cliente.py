from usuario import Usuario

class Cliente(Usuario):

    def __init__(self, antiguedad_compras, compras_realizadas, comida_favorita, identificadorC, nombreC, apellidoC, emailC, telefonoC, dniC):
        super().__init__(identificadorC, nombreC, apellidoC, emailC, telefonoC, dniC)
        self.antiguedad_compras = antiguedad_compras
        self.compras_realizadas = compras_realizadas
        self.comida_favorita = comida_favorita
