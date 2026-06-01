from cuenta import cuenta

class Banco:

    def __init__(self):
        self.cuentas = []

    def agregar_cuenta(self, nueva_cuenta):
        self.cuentas.append(nueva_cuenta)

    def transferir(self, origen, destino, cantidad):
        if origen.retiro(cantidad):  # ← "retiro" no "retirar"
            destino.deposito(cantidad)
            return True
        return False
