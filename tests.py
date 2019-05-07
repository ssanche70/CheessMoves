from unittest import TestCase
from movimientos import *

class Test_movimientos(TestCase):

    def test_tablero_a_cadena(self):
        dado = []
        espero = ""
        obtengo = tablero_a_cadena(dado)
        self.assertEquals(espero, obtengo)

    def test_obtener_nombre_pieza(self):
        dado = 'k'
        espero = "caballo blanco"
        obtengo = obtener_nombre_pieza(dado)
        self.assertEquals(espero, obtengo)