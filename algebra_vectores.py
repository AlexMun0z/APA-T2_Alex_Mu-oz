class Vector:
    vector = []
    def __init__(self, numeros):
        """
        Constructor de la clase Vector
        """
        self.vector = [numero for numero in numeros]

    def __repr__(self):
        """
        Representación del vector que permite construiur uno nuevo idéntico
        """
        return 'Vector(' + repr(self.vector) + ')'

    def __str__(self):
        """
        Representación 'bonita' del vector
        """
        str_ = '['
        for component in self.vector:
            str_ += ' ' + str(component)
        str_ += ' ]'
        return str_

    def __getitem__(self, key):
        """
        Devuelve el elemento 'keyesimo' del vector
        """
        return self.vector[key]

    def __setitem__(self, key, value):
        """
        Fija el valor de una componente del vector
        """
        self.vector[key] = value

    def __len__(self):
        """
        Devuelve la longitud del vector
        """
        return len(self.vector)

    def __add__(self, other):
        """
        Suma el vector otro vector o una constante
        """
        if isinstance(other, (int, float, complex)):
            return Vector([elemento + other for elemento in self])
        else:
            return Vector([uno + otro for uno, otro in zip(self, other)])

    __radd__  = __add__  

    def __neg__(self):
        """
        Invierte el signo del vector
        """
        return Vector([-elemento for elemento in self])

    def __sub__(self, other):
        """
        Resta el vector otro vector o constante
        """
        return -(other + (-self))

    def __rsub__(self,other):
        """
        Método reflejado de la resta, usado cuándo el primer elemento no pertenece a la clase Vector
        """
        return -self + other

 # Multiplicación de los elementos de 2 vectores(Hadamard) o de un vector por un escalar

    def __mul__(self,other):
        """
        Producto de Hadamard
        
        >>> v1 = Vector([1, 2, 3])
        >>> v1 * 2
        Vector([2, 4, 6])
        >>> v1 = Vector([1, 2, 3])
        >>> v2 = Vector([4, 5, 6])
        >>> v1 * v2
        Vector([4, 10, 18])

        >>> v1 = Vector([1, 2])
        >>> v2 = Vector([1, 2, 3])
        Traceback (most recent call last):
        ...
        ValueError: Los vectores deben tener la misma dimensión (Hadamard)
        """

        if isinstance(other,Vector):
            if len(self.vector) != len(other.vector):
                raise ValueError("Los vectores deben tener la misma dimensión (Hadamard)")
            return Vector([uno * otro for uno, otro in zip(self.vector, other.vector)])
        elif isinstance(other, (int, float)):
            return Vector([elemento * other for elemento in self.vector])
        else:
            return NotImplemented

    def __rmul__(self,other):
        """
        Multiplicación de un vector por un escalar
        
        Test unitario:
        >>> v1 = Vector([1, 2, 3])
        >>> 2 * v1
        Vector([2, 4, 6])
        """

        if isinstance(other,(int, float)):
            return self.__mul__(other)
        else:
            return NotImplemented


    def __matmul__(self,other):
        """
        Producto escalar de dos vectores

        Test unitario:
        >>> v1 = Vector([1, 2, 3])
        >>> v2 = Vector([4, 5, 6])
        >>> v1 @ v2
        32
        >>> v1 = Vector([1, 2])
        >>> v2 = Vector([4, 5, 6])
        Traceback (most recent call last):
        ...
        ValueError: Los vectores deben tener la misma dimensión para el producto escalar
        """

        if isinstance(other, Vector):
            if len(self.vector) != len(other.vector):
                raise ValueError("Los vectores deben tener la misma dimensión para el producto escalar")
            return sum(uno * otro for uno, otro in zip(self.vector, other.vector))
        else:
            return NotImplemented

    def __rmatmul__(self,other):
        """
        Producto escalar cuando el vector está a la derecha del operador @

        Test unitario:
        >>> v1 = Vector([1, 2, 3])
        >>> v2 = Vector([4, 5, 6])
        >>> v2 @ v1 
        32
        """
        return self.__matmul__(other)


 # Obtención de las componentes normal y paralela de un vector respecto al otro 

    def __floordiv__(self,other):
        """
        Componente paralela de self a other (v1//v2)

        Test unitario:
        >>> v1 = Vector([2, 1, 2])
        >>> v2 = Vector([0.5, 1.0, 0.5])
        >>> v1 // v2
        Vector([1.0, 2.0, 1.0])
        """

        if isinstance(other,Vector):
            norm_squared = other @ other 
            if norm_squared == 0:
                raise ValueError("No se puede proyectar sobre el vector 0")
            scalar = (self @ other) / norm_squared
            return Vector([scalar * elemento for elemento in other.vector])

    def __rfloordiv__(self,other):
        """
        Componente paralela de other cuando está a la izquierda del operador //
        """
        if isinstance(other, Vector):
            return other // self

    def __mod__(self,other):
        """
        Componente normal (perpendicular) de self respecto a other:

        Test unitario:
        >>> v1 = Vector([2, 1, 2])
        >>> v2 = Vector([1.0, 2.0, 1.0])
        >>> v1 % v2 
        Vector([1.0, -1.0, 1.0])
        >>> (v1 // v2) + (v1 % v2)
        Vector([2, 1, 2])
        
        """
        if isinstance(other, Vector):
            return self - (self // other)
        return NotImplemented

    def __rmod__(self,other):
        """
        Componente perpendicular cuando other está a la izquierda del operador %.

        """
        if isinstance(other, Vector):
            return other % self
        return NotImplemented

if __name__  == " __main__":
    import doctest
    doctest.testmod()
    
    
