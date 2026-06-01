
class cuenta:
    """Representa una cuenta bancaria con operaciones básicas de depósito y retiro."""

    def _init_(self, cliente, cuenta, saldo=0):
        """cliente: nombre del clientenombre del dueño de la cuenta
         cuenta: número de cuenta
        saldo: dinero inicial, por defecto 0"""
        self.cliente = cliente
        self.cuenta = cuenta
        self.saldo = saldo

    def deposito(self, cantidad):
        """Suma la cantidad al saldo si es mayor a 0.
        Retorna True si se hizo el depósito, False si no."""
        if cantidad > 0:
            self.saldo += cantidad
            return True
        return False

    def retiro(self, cantidad):
        """Resta la cantidad al saldo si es mayor a 0 y hay suficiente dinero.
        Retorna True si se pudo retirar, False si no."""
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            return True
        return False


def main():
    """Punto de entrada del programa."""
    pass


if __name__ == "__main__":
    main()