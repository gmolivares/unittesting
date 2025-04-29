def sum(a,b):
    """
    >>> sum(5,7)
    12

    >>> sum(4,-4)
    0
    """
    return a+b

def subtract(a,b):
    return a-b 

def multiply(a,b):
    return a*b

def div(a,b):
    """
    >>> div(10,0)
    Traceback (most recent call last):
    ValueError: La Division por cero no esta permitida
    """
    if b == 0:
        raise ValueError("La Division por cero no esta permitida")
    return a/b