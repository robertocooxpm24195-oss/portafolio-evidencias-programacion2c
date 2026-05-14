class perro:
    especie = "Canis lupus familiaris"
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    #constructor para inicializar los atributos del perro
    def __init__(self, nombre,raza,edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
    #metodo para imprimir los datos del perro
    def imprimirDatos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad} edad")

    def main():
        perro1 = perro("max", "labrador", 5)
        perro1.imprimirDatos()
        perro2 = perro("Bella", "golden retriever", 3)
        perro2.imprimirDatos()
        perro3 = perro("max", "Bulldog", 7)
        perro3.imprimirDatos()
        perro4 = perro("Dante",)
        perro4.imprimirDatos()
        perro2 = perro("pastor belga", )
        perro2.imprimirDatos()
        perro5 = perro("raya", "siames", 1)
        perro5.imprimirDatos()

    if __name__ == "__main__":
        "main"