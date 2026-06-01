puntos = 10 

def calcular_puntos(bono):
    global puntos
    puntos = puntos + bono
    return puntos

print(calcular_puntos(5))
print(puntos)