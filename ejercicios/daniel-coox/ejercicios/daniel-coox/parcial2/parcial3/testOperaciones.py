import unittest
from parcial2.calculadoraBasica import suma, resta, multi, division 

class testOperaciones(unittest.testcase):

    def tes_suma_positivo (self):
        self.asserEqual(suma(300,3),303)

    def test_suma_negativos(self):
        self.assertEqual(suma(-4,-6),-10)

    def text_resta_basica(self):
        self,assertEqual(resta(10,5), 5)

    def test_resta_negativa(self):
        self.assertEqual(resta(10,30), -20)

    def test_resta_negativos(self):
        self.assertEqual(resta(-5,-5), 0)

    if  __name__ == "__main__":
        unittest.main()