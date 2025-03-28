def sum(a,b):
    return a+b

def subtract(a,b):
    return a-b 

def multiply(a,b):
    return a*b

def div(a,b):
    if b == 0:
        raise ValueError("La Division por cero no esta permitida")
    return a/b