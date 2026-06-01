import unittest

from cuenta import cuenta 
from banco import Banco

class testIntegracionBanco(unittest.TestCase):

    def setUp(self):
        self.cuenta1 =  cuenta("Fulanito perez", "001", 1000)
        self.cuenta2 = cuenta("perezcila Sachez", "002")

        self.banco = Banco()

    def test_transferencia_exitosa(self):
        resultado = self.banco.transferir(self.cuenta1, self.cuenta2, 350)
        self.asserTrue(resultado, "Deberia realizarce de manera correcta la transferecia")
        self.asserEqual(self.cuenta1.saldo, 650, "El saldo de l cuenta1 deberia ser 650")
        self.asserEqual(self.cuenta2.saldo, 350, "El saldo de la cuenta destino deberia ser 350")

    def test_transferecia_saldo_insuficiente(self):
        resultado = self.banco.transferir(self.cuenta1, self.cuenta2, 1200)
        self.assertFalse(resultado, "la transferecia no se deberia realixar al no disponer ")
        self.assertEqual(self.cuenta1.saldo, 1000, "el saldo debria mantenerse sin cambios")
        self.asserEqual(self.cuenta2.saldo, 0, "El saldo de la cuenta destino deberia ser 0")
        
        if __name__== "__main__":
            unittest.main()