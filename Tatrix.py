#!/bin/bash

from termcolor import colored
import pyfiglet
import random

text = pyfiglet.figlet_format("TATRIX")

colored_text = ""
colors = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]

for char in text:
    random_color = random.choice(colors)
    colored_char = colored(char, random_color)
    colored_text += colored_char

print(colored_text)
print("_____________By Josh V1.0")
print("")


def calcular_binario_decimal():
    try:
        valor_binario = input("Ingrese un número binario: ")
        decimal = int(valor_binario, 2)
        print("Procedimiento: {} en binario es igual a {} en decimal.".format(valor_binario, decimal))
    except ValueError:
        print("El número binario ingresado es inválido.")


def calcular_decimal_binario():
    try:
        valor_decimal = int(input("Ingrese un número decimal: "))
        binario = bin(valor_decimal)[2:]
        print("Procedimiento: {} en decimal es igual a {} en binario.".format(valor_decimal, binario))
    except ValueError:
        print("El número decimal ingresado es inválido.")


def calcular_decimal_hexadecimal():
    try:
        valor_decimal = int(input("Ingrese un número decimal: "))
        hexadecimal = hex(valor_decimal)[2:]
        print("Procedimiento: {} en decimal es igual a {} en hexadecimal.".format(valor_decimal, hexadecimal))
    except ValueError:
        print("El número decimal ingresado es inválido.")


def calcular_hexadecimal_decimal():
    try:
        valor_hexadecimal = input("Ingrese un número hexadecimal: ")
        decimal = int(valor_hexadecimal, 16)
        print("Procedimiento: {} en hexadecimal es igual a {} en decimal.".format(valor_hexadecimal, decimal))
    except ValueError:
        print("El número hexadecimal ingresado es inválido.")


def calcular_decimal_octal():
    try:
        valor_decimal = int(input("Ingrese un número decimal: "))
        octal = oct(valor_decimal)[2:]
        print("Procedimiento: {} en decimal es igual a {} en octal.".format(valor_decimal, octal))
    except ValueError:
        print("El número decimal ingresado es inválido.")


def calcular_octal_decimal():
    try:
        valor_octal = input("Ingrese un número octal: ")
        decimal = int(valor_octal, 8)
        print("Procedimiento: {} en octal es igual a {} en decimal.".format(valor_octal, decimal))
    except ValueError:
        print("El número octal ingresado es inválido.")


def calcular_decimal_grey():
    try:
        valor_decimal = int(input("Ingrese un número decimal: "))
        grey = valor_decimal ^ (valor_decimal >> 1)
        print("Procedimiento: El valor grey de {} es {}.".format(valor_decimal, grey))
    except ValueError:
        print("El número decimal ingresado es inválido.")


def calcular_decimal_ascii():
    try:
        valor_decimal = int(input("Ingrese un número decimal: "))
        ascii_char = chr(valor_decimal)
        print("Procedimiento: El valor ASCII de {} es {}.".format(valor_decimal, ascii_char))
    except ValueError:
        print("El número decimal ingresado es inválido.")


def calcular_decimal_exceso_tres():
    try:
        valor_decimal = int(input("Ingrese un número decimal: "))
        exceso_tres = valor_decimal + 3
        print("Procedimiento: El valor en exceso de tres de {} es {}.".format(valor_decimal, exceso_tres))
    except ValueError:
        print("El número decimal ingresado es inválido.")


# Función principal
def menu_principal():
    try:
        while True:
            print("Por favor, elija una opción:")
            print("0. Calculadora de binario a decimal y viceversa")
            print("1. Calculadora  De Decimal a hexadecimal y viceversa")
            print("2. Calculadora  De Decimal a Octagonal y viceversa")
            print("3. Calculadora  De Decimal a grey")
            print("4. Caculadora De decimal a ASCII")
            print("5. Calculadora Decimal a exceso de 3")
            print("6. Salir")

            opcion = input("Opción: ")

            if opcion == "0":
                print("\n--- Calculadora de binario a decimal y viceversa ---")
                subopcion = input
                print("Seleccione una opción:")
                print("  0. Binario a Decimal")
                print("  1. Decimal a Binario")
                subopcion = input("Subopción: ")
                if subopcion == "0":
                    print("\n--- Binario a Decimal ---")
                    calcular_binario_decimal()
                elif subopcion == "1":
                    print("\n--- Decimal a Binario ---")
                    calcular_decimal_binario()
                else:
                    print("Opción inválida.")

            elif opcion == "1":
                print("\n--- De Decimal a hexadecimal y viceversa ---")
                print("Seleccione una opción:")
                print("  0. Decimal a Hexadecimal")
                print("  1. Hexadecimal a Decimal")
                subopcion = input("Subopción: ")
                if subopcion == "0":
                    print("\n--- Decimal a Hexadecimal ---")
                    calcular_decimal_hexadecimal()
                elif subopcion == "1":
                    print("\n--- Hexadecimal a Decimal ---")
                    calcular_hexadecimal_decimal()
                else:
                    print("Opción inválida.")

            elif opcion == "2":
                print("\n--- De Decimal a Octagonal y viceversa ---")
                print("Seleccione una opción:")
                print("  0. Decimal a Octal")
                print("  1. Octal a Decimal")
                subopcion = input("Subopción: ")
                if subopcion == "0":
                    print("\n--- Decimal a Octal ---")
                    calcular_decimal_octal()
                elif subopcion == "1":
                    print("\n--- Octal a Decimal ---")
                    calcular_octal_decimal()
                else:
                    print("Opción inválida.")

            elif opcion == "3":
                print("\n--- De Decimal a grey ---")
                calcular_decimal_grey()

            elif opcion == "4":
                print("\n--- De decimal a ASCII ---")
                calcular_decimal_ascii()

            elif opcion == "5":
                print("\n--- Decimal a exceso de 3 ---")
                calcular_decimal_exceso_tres()

            elif opcion == "6":
                print("¡Hasta luego!")
                break

            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
    except KeyboardInterrupt:
        print("\nPrograma cancelado por el usuario.")


# Llamada a la función principal
menu_principal()
