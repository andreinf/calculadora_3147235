from operaciones.operaciones import sumar, restar, multiplicar, dividir, potencia, division_entera

def main():
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        operador = input("Introduce el operador (+, -, *, /, **, //): ")

        if operador == "+":
            resultado = sumar(num1, num2)
        elif operador == "-":
            resultado = restar(num1, num2)
        elif operador == "*":
            resultado = multiplicar(num1, num2)
        elif operador == "/":
            resultado = dividir(num1, num2)
        elif operador == "**":
            resultado = potencia(num1, num2)
        elif operador == "//":
            resultado = division_entera(num1, num2)
        else:
            raise ValueError("Operador no válido")

        print(f"El resultado de {num1} {operador} {num2} es: {resultado}")

    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()
