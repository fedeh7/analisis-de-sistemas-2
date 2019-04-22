from cocinero import Cocinero
from delivery import Delivery
from cliente import Cliente
from admin import Admin

prueba = Cocinero("chef", 1, "Test", "test", "A@A", 123, 987)

prueba.informacion()

'''

Asosiacion, agregacion, composicion, herencia, interfaz, clases abstractas
la interfaz es una abstraccion maxima, una interfaz solo tiene metodos abstractos y no tiene propiedas, por ende no puedo hacer asosiciones con esta, no puede tener atributos pero si puede tener constantes
una clase abstracta, puede tener metodos concretos como abstractos, puede tener atributos y puede tener constantes, no se puede instanciar

'''