import unittest
from cuenta import cuenta

class testCuenta(unittest.TestCase):
   
    def setUp(self):
        """    Este método se ejecuta anntes de cada prueba
        """
        self.cuenta = cuenta("Fulanito perez Mengano", "001")

    # ________ PRUBEAS DEL CONSTRUCTOR _________

    def test_validar_saldo(self):
        self.assertEqual(self.cuenta.saldo, 0, "El saldo inicial debe ser 0 por defecto")

    def test_validar_cliente(self):
        self.assertEqual(self.cuenta.cliente,"Fulanito perez Mengano","El nombre del cliente no se asignó correctamente")
            
    # ________ PRUEBAS DEPOSITOS _________

    def test_depositar_dinero_valido(self):
        result = self.cuenta.deposito(500)
        self.assertTrue(result)
        self.assertEqual(self.cuenta.saldo, 500, "El saldo actual deberia ser de 500.00")

    def test_depositar_cantidad_negativa(self):
        self.assertFalse(self.cuenta.saldo, 0, "El saldo actual deberia ser de 0")

    #test para validar deposito en 0
    def test_depositar_cantidad_cero(self):
        result = self.cuenta.deposito(0)
        self.assertFalse(result, "El depósito con cantidad 0 debe retornar False")
        self.assertEqual(self.cuenta.saldo, 0, "El saldo debe permanecer en 0")


    # ________ PRUEBAS DE RETIROS _________

    # 1. test para validar retiro con cantidad 0
    def test_retirar_cantidad_cero(self):
        self.assertFalse(self.cuenta.retiro(0),"El retiro con cantidad 0 debe retornar False")

    # 2. test para validar retiro con cantidad negativa
    def _test_retirar_cantidad_negativa(self):
        self.assertFalse(self.cuenta.retiro(-100),"El retiro con cantidad negativa debe retornar False")

    # 3. test para validar cantidad mayor al saldo
    def test_retirar_cantidad_mayor_al_saldo(self):
        self.cuenta.deposito(200)
        self.assertFalse(self.cuenta.retiro(300),"El retiro con cantidad mayor al saldo debe retornar False")