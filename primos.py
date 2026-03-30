"""
primos.py

Alex Muñoz Paton 

Módulo de manejo de números primos

"""

print(__name__)

def esPrimo(numero):

    """
    True si el número es primo, False si no lo es 
    El argumento tiene que ser un número natural > 1, si es 1, se eleva a TypeError y finaliza la ejecución

    >>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    >>> esPrimo(1)
    Traceback (most recent call last):
        ...
    TypeError: El argumento debe ser un número natural mayor que 1
    """
    
    if not numero > 1:
        raise TypeError("El argumento debe ser un numero natural mayor que 1")
    if numero == 2:
        return True
    if numero % 2 == 0 and  numero != 2:
        return False
    for divisor in range(3, int(numero **0.5)+1, 2):
        if numero % divisor == 0:
            return False 
    return True


def primos(numero):

    """
    Esta función devuelve una tupla con todos los numeros primos de menores que el argumento
    Test unitario de la función primos:

    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

    """
    return tuple(n for n in range (2,numero) if esPrimo(n))

def descompon(numero):
    
    """
    Esta función devuelve un numero descompuesto en factores de numeros primos

    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)
    """
    factores = []
    divisor = 2 
    while divisor *divisor <= numero:
        while numero % divisor == 0:
            factores.append(divisor)
            numero = numero // divisor
        if divisor == 2:
            divisor += 1
        else:
            divisor += 2
    if numero > 1:
        factores.append(numero)
    return tuple(factores)

def mcd_descompon(numero1, numero2):

    """
    Esta función devuelve el máximo comun divisor de dos elementos usando la función descompon préviamente definida

    >>> mcd_descompon(924, 780)
    12
    """
    factores1 = list(descompon(numero1))
    factores2 = list(descompon(numero2))
    factores_comunes = []
    for factor in factores1:
        if factor in factores2:
            factores_comunes.append(factor)
            factores2.remove(factor)  
    resultado = 1
    for factor in factores_comunes:
        resultado *= factor
    return resultado 


def mcm_descompon(numero1, numero2):

    """
    Esta función devuelve el mínimo común múltiple de dos elementos usando la función descompon préviamente definida

    >>> mcm_descompon(90, 14)
    630
    """
    factores1 = list(descompon(numero1))
    factores2 = list(descompon(numero2))
    for factor in factores1:
        if factor in factores2:
            factores2.remove(factor) 
    factores_union = factores1 + factores2
    resultado = 1
    for factor in factores_union:
        resultado *= factor
    return resultado
    
def mcd(*numeros):
    """
    Esta función devuelve el máximo común divisor de 2  o más números
    
    >>> mcd(924, 780)
    12
    >>> mcd(840, 630, 1050, 1470)
    210
    """
    resultado = numeros[0]
    for numero in numeros[1:]:
        while numero != 0:
            resto = resultado % numero
            resultado = numero
            numero =resto
    return resultado 

def mcm(*numeros):

    """
    Esta función devuelve el mínimo común múltiplo de dos o más números.

    >>> mcm(90, 14)
    630
    >>> mcm(42, 60, 70, 63)
    1260
    """
    resultado = numeros[0]
    for numero in numeros[1:]:
        resultado = resultado * numero // mcd(resultado, numero) 
    return resultado

if __name__ == "__main__":
    import doctest
    doctest.testmod()
