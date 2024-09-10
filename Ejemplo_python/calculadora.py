import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero no permitida."
    return a / b

def raiz_cuadrada(a):
    if a < 0:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo."
    return math.sqrt(a)

def potencia(a, b):
    return a ** b

def mostrar_menu():
    print("\nCalculadora")
    print("Seleccione una opción:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Raíz Cuadrada")
    print("6. Potencia")
    print("7. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingresa una opción: ")

        if opcion == '7':
            print("Usuario salio del programa")
            break

        if opcion in ['1', '2', '3', '4', '6']:
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingrese el segundo número: "))

        elif opcion == '5':
            a = float(input("Ingrese el número: "))

        if opcion == '1':
            print(f"Resultado: {suma(a, b)}")
        elif opcion == '2':
            print(f"Resultado: {resta(a, b)}")
        elif opcion == '3':
            print(f"Resultado: {multiplicacion(a, b)}")
        elif opcion == '4':
            print(f"Resultado: {division(a, b)}")
        elif opcion == '5':
            print(f"Resultado: {raiz_cuadrada(a)}")
        elif opcion == '6':
            print(f"Resultado: {potencia(a, b)}")
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()
