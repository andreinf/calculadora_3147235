def sumar (a, b):
    return a + b

def restar (a, b):
    return a - b

def multiplicar (a, b):
    return a * b
# operaciones.
#def se usa para definir funciones
# y abajo se retorna una operacion o funcion de tenga esta def
#valueError es un comando donde un texto se muestra como error
 # operaciones.py

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def potencia(a, b):
    try:
        return a ** b  # Intentamos realizar la operación de potencia
    except OverflowError:
        raise ValueError("El resultado es demasiado grande para manejarlo")  # Excepción si el resultado es demasiado grande

def division_entera(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a // b