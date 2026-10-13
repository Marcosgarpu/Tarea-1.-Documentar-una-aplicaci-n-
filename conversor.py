"""Conversor de temperaturas entre Celsius, Fahrenheit y Kelvin."""


def celsius_a_fahrenheit(c):
    return c * 9 / 5 + 32


def fahrenheit_a_celsius(f):
    return (f - 32) * 5 / 9


def celsius_a_kelvin(c):
    return c + 273.15


def kelvin_a_celsius(k):
    return k - 273.15


def mostrar_menu():
    print("\n=== CONVERSOR DE TEMPERATURAS ===")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Celsius a Kelvin")
    print("4. Kelvin a Celsius")
    print("5. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ")

        if opcion == "5":
            print("¡Hasta pronto!")
            break

        if opcion not in ("1", "2", "3", "4"):
            print("Opción no válida.")
            continue

        try:
            valor = float(input("Introduce la temperatura: "))
        except ValueError:
            print("Debes introducir un número.")
            continue

        if opcion == "1":
            print(f"{valor} °C = {celsius_a_fahrenheit(valor):.2f} °F")
        elif opcion == "2":
            print(f"{valor} °F = {fahrenheit_a_celsius(valor):.2f} °C")
        elif opcion == "3":
            print(f"{valor} °C = {celsius_a_kelvin(valor):.2f} K")
        elif opcion == "4":
            print(f"{valor} K = {kelvin_a_celsius(valor):.2f} °C")


if __name__ == "__main__":
    main()