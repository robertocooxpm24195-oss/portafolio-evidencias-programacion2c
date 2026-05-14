class Ave:
    def __init__(self,color = "verde"):
        self.color = color

    def volar(self):
        print("puedo volar")

class canario(Ave):
    def __init__(self,color,nombre):
        super().__init__(color)
        self.nombre = nombre

    def informacion(self):
        pass

canario = canario("amarillo","fulanito")
print(canario.color)
canario.volar()
print(canario.color)