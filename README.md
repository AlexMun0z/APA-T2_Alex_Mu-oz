# Segunda tarea de APA 2026: Manejo de números primos

> [!Caution]
>
> El objetivo de esta tarea es manejar los tipos de datos y las estructuras de control de flujo de
> Python. Existen bibliotecas que resuelven los apartados del enunciado de una manera más eficiente
> y, sin duda, más sencilla, pero su uso está prohibido.
>
> Además, se valorará también el uso de Markdown en la redacción del fichero README.md; en concreto,
> la inclusión de código fuente con las herramientas propias de Markdown para su realce sintáctico, y
> la inclusión de imágenes con las capturas de pantalla solicitadas. El fichero README.md deberá ser
> visualizado correctamente desde la página principal del repositorio GitHub del alumno sin ninguna
> intervención por parte del profesor.
>
> Dispone del fichero MARKDOWN.md con información básica para el uso de Markdown, así como con enlaces
> a la documentación oficial del mismo.
>
> ¿Quiere saber más?, consulte con el profesorado.
  
## Nom i cognoms

> [!Important]
> Introduzca a continuación su nombre y apellidos:
>
> Alex Muñoz Paton

## Fichero `primos.py`

- El alumno debe escribir el fichero `primos.py` que incorporará distintas funciones relacionadas con el manejo
  de los números primos.

- El fichero debe incluir una cadena de documentación que incluirá el nombre del alumno y los tests unitarios
  de las funciones incluidas.

- Cada función deberá incluir su propia cadena de documentación que indicará el cometido de la función, los
  argumentos de la misma y la salida proporcionada.

- Se valorará lo pythónico de la solución; en concreto, su claridad y sencillez, y el uso de los estándares marcados
  por PEP-8. También se valorará su eficiencia computacional.

### Determinación de la *primalidad* y descomposición de un número en factores primos

Incluya en el fichero `primos.py` las tres funciones siguientes:

- `esPrimo(numero)`   Devuelve `True` si su argumento es primo, y `False` si no lo es.
  - Se debe considerar que `numero` es un número natural y mayor que uno.
  - En caso contrario, la función debe elevar la excepción `TypeError` y finalizar la ejecución.
- `primos(numero)`    Devuelve una **tupla** con todos los números primos menores que su argumento.
- `descompon(numero)` Devuelve una **tupla** con la descomposición en factores primos de su argumento.

### Obtención del mínimo común múltiplo y el máximo común divisor

Usando las tres funciones del apartado anterior (y cualquier otra que considere conveniente añadir), escriba otras
dos que calculen el máximo común divisor y el mínimo común múltiplo de sus argumentos:

- `mcm(numero1, numero2)`:  Devuelve el mínimo común múltiplo de sus argumentos.
- `mcd(numero1, numero2)`:  Devuelve el máximo común divisor de sus argumentos.

Estas dos funciones deben cumplir las condiciones siguientes:

- Aunque se trate de una solución sub-óptima, en ambos casos deberá partirse de la descomposición en factores
  primos de los argumentos usando las funciones del apartado anterior.

- Aunque también sea sub-óptimo desde el punto de vista de la programación, ninguna de las dos funciones puede
  depender de la otra; cada una debe programarse por separado.

### Obtención del mínimo común múltiplo y el máximo común divisor para un número arbitrario de argumentos

Modifique las funciones `mcm()` y `mcd()`, para que calculen el mínimo común múltiplo y el máximo común divisor
para un número arbitrario de argumentos:

- `mcm(*numeros)`:  Devuelve el mínimo común múltiplo de sus argumentos.
- `mcd(*numeros)`:  Devuelve el máximo común divisor de sus argumentos.

### Tests unitarios

La cadena de documentación del fichero debe incluir los tests unitarios de las cinco funciones. En concreto, deberán
comprobarse las siguientes condiciones:

- `esPrimo(numero)`:  Al ejecutar `[ numero for numero in range(2, 50) if esPrimo(numero) ]`, la salida debe ser
                      `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]`.
- `primos(numeor)`: Al ejecutar `primos(50)`, la salida debe ser `(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)`.
- `descompon(numero)`: Al ejecutar `descompon(36 * 175 * 143)`, la salida debe ser `(2, 2, 3, 3, 5, 5, 7, 11, 13)`.
- `mcm(num1, num2)`: Al ejecutar `mcm(90, 14)`, la salida debe ser `630`.
- `mcd(num1, num2)`: Al ejecutar `mcd(924, 780)`, la salida debe ser `12`.
- `mcm(numeros)`: Al ejecutar `mcm(42, 60, 70, 63)`, la salida debe ser `1260`.
- `mcd(numeros)`: Al ejecutar `mcd(840, 630, 1050, 1470)`, la salida debe ser `210`.

### Entrega

#### Ejecución de los tests unitarios

Inserte a continuación una captura de pantalla que muestre el resultado de ejecutar el fichero `primos.py` con la opción
*verbosa*, de manera que se muestre el resultado de la ejecución de los tests unitarios.
##### Código para ejecutar los test unitarios
<img width="495" height="238" alt="image" src="https://github.com/user-attachments/assets/708916b8-4533-49de-9025-93e22144d11a" />

###### Test unitario de esPrimo
<img width="504" height="97" alt="image" src="https://github.com/user-attachments/assets/82ec1365-185e-4ac9-8a19-7c6cc117337a" />

###### Test unitario de esPrimo(1)
<img width="646" height="443" alt="image" src="https://github.com/user-attachments/assets/cb587276-1ddb-4bbb-8adb-43cd55d2c5be" />

###### Test unitario de primos
<img width="494" height="95" alt="image" src="https://github.com/user-attachments/assets/96d82484-cff4-4787-829a-1b497053b661" />

###### Test unitario de descompon
<img width="279" height="100" alt="image" src="https://github.com/user-attachments/assets/23bf41e8-b30b-4508-bdb2-8499eb933981" />

###### Test unitario de mcd_descompon
<img width="224" height="100" alt="image" src="https://github.com/user-attachments/assets/38c93a89-a827-45a0-8ce7-ad3a786743f6" />

###### Test unitario de mcm_descompon
<img width="212" height="95" alt="image" src="https://github.com/user-attachments/assets/1345f38a-94a7-4682-adf1-dea60698fad0" />

###### Test unitario de mcd
<img width="242" height="192" alt="image" src="https://github.com/user-attachments/assets/19f7a5e7-277c-4047-8a19-afa896943be1" />

###### Test unitario de mcm
<img width="193" height="194" alt="image" src="https://github.com/user-attachments/assets/6a79861a-7ac5-4e80-8b3f-d83532bdec83" />

###### Resultados Test unitario
<img width="325" height="317" alt="image" src="https://github.com/user-attachments/assets/904b83a7-0354-49ee-b668-f89dbba2e981" />



#### Código desarrollado

Inserte a continuación el contenido del fichero `primos.py` usando los comandos necesarios para que se realice el
realce sintáctico en Python del mismo.
##### Código Completo

```python
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


```
##### Funciones desglosadas 
###### esPrimo
``` python
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
```
###### primos
``` python
def primos(numero):

    """
    Esta función devuelve una tupla con todos los numeros primos de menores que el argumento
    Test unitario de la función primos:

    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

    """
    return tuple(n for n in range (2,numero) if esPrimo(n))
```
###### descompon
``` python
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
```
###### mcd_descompon
``` python
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
```
###### mcm_descompon
``` python
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
```
###### mcd
``` python
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
```
###### mcm
``` python
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
```
#### Subida del resultado al repositorio GitHub ¿y *pull-request*?

El fichero `primos.py`, la imagen con la ejecución de los tests unitarios y este mismo fichero, `README.md`, deberán
subirse al repositorio GitHub mediante la orden `git push`. Si los profesores de la asignatura consiguen montar el
sistema a tiempo, la entrega se formalizará realizando un *pull-request* al propietario del repositorio original.

El fichero `README.md` deberá respetar las reglas de los ficheros Markdown y visualizarse correctamente en el repositorio,
incluyendo la imagen con la ejecución de los tests unitarios y el realce sintáctico del código fuente insertado.
