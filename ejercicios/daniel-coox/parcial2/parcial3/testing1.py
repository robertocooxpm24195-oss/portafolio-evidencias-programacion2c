def calcular_media(*args):
    """Devuelve el valor de la media o promedio de un conjunto de datos numericos.

    Args:
        *args (int): un numero variable de argumentos que representan los 
    returns:
        (float): El valor de la media o promedio de los datos numericos. 
 """


    return (sum(*args)/len(*args))

assert(calcular_media([3,4,5]) == 4.0)
assert(calcular_media([10,20,30]) == 20.0)