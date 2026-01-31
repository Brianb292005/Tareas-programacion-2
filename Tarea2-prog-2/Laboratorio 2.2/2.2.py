# Manipulacion de strings:

texto = "Programar en Python es divertido"

print("Texto original:", texto)

print("Mayúsculas:", texto.upper())

print("Minúsculas:", texto.lower())

print("Reemplazo:", texto.replace("Python", "Java"))

print("Cantidad de caracteres:", len(texto))

# indexación y slicing:

palabra = "Programacion"

print("Primera letra:", palabra[0])

print("Última letra:", palabra[-1])

print("Primeras 5 letras:", palabra[:5])

print("Desde la posición 6:", palabra[6:])

print("Salto de 2 en 2:", palabra[::2])

# uso de listas y tuplas:

lenguajes = ["Python", "Java", "C++"]

lenguajes.append("JavaScript")

print("Lista de lenguajes:", lenguajes)


numeros = (10, 20, 30)

print("Tupla de números:", numeros)

print("Primer número:", numeros[0])