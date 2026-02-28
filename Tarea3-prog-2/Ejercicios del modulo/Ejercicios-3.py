# EJERCICIO 1:

edad  = 18

if edad >= 18:
    print("Eres mayor de edad")     
    
else:
    print("Eres menor de edad")

# EJERCICIO 2:

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

mayor = num1

if num2 > mayor:
    mayor = num2

if num3 > mayor:
    mayor = num3

print("El número mayor es:", mayor)

# EJERCICIO 3:

usuario = input("Ingrese usuario: ")
password = input("Ingrese password: ")

if (usuario == "admin" and password == "1234") or (usuario == "profesor" and password == "abcd"):
    print("Acceso concedido")
else:
    print("Acceso denegado")
    
# EJERCICIO 4:

edad = int(input("Ingrese su edad: "))
ingresos = float(input("Ingrese sus ingresos mensuales: "))
lista_negra = input("¿Está en lista negra? (si/no): ").lower()

if 21 <= edad <= 65 and ingresos > 30000 and lista_negra == "no":
    print("Crédito aprobado ✅")
else:
    print("Crédito denegado ❌")
    if not (21 <= edad <= 65):
        print("  - Edad fuera del rango permitido (21-65 años).")
    if ingresos <= 30000:
        print("  - Ingresos insuficientes (deben ser mayores a 30,000).")
    if lista_negra == "si":
        print("  - El cliente está en lista negra.")
        
# EJERCICIO 5:

suma = 0
cantidad = 0

while True:
    numero = float(input("Ingrese un número (0 para terminar): "))
    
    if numero == 0:
        break
    
    suma += numero
    cantidad += 1

if cantidad > 0:
    promedio = suma / cantidad
    print(f"\nCantidad de números ingresados: {cantidad}")
    print(f"Suma total: {suma}")
    print(f"Promedio: {promedio:.2f}")
else:
    print("No ingresó ningún número.")
    
# EJERCICIO 6:

for i in range(1, 11):
    print(f"\n--- Tabla del {i} ---")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
        
# EJERCICIO 7:

nombres = ["Ana", "Luis", "Pedro", "Marta"]

iterador = iter(nombres)

while True:
    try:
        nombre = next(iterador)
        print(nombre)
    except StopIteration:
        print("Se recorrieron todos los nombres.")
        break
    
# EJERCICIO 8:

def calcular_descuento(precio, porcentaje):
    descuento = precio * (porcentaje / 100)
    precio_final = precio - descuento
    return precio_final

precio = float(input("Ingrese el precio original: "))
porcentaje = float(input("Ingrese el porcentaje de descuento: "))

resultado = calcular_descuento(precio, porcentaje)
print(f"Precio con descuento del {porcentaje}%: ${resultado:.2f}")

# EJERCICIO 9:

def sumar(*args):
    total = 0
    for numero in args:
        total += numero
    return total

print(sumar(1, 2, 3, 4))       # → 10
print(sumar(5, 10))            # → 15
print(sumar(1, 2, 3, 4, 5, 6)) # → 21

# EJERCICIO 10:

def factorial(n):
    if n < 0:
        return "Error: no se aceptan números negativos."
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

numero = int(input("Ingrese un número para calcular su factorial: "))
print(f"El factorial de {numero} es: {factorial(numero)}")

# EJERCICIO 11:

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def operar(a, b, funcion):
    return funcion(a, b)

print(operar(10, 5, sumar))       # → 15
print(operar(10, 5, restar))      # → 5
print(operar(10, 5, multiplicar)) # → 50

# EJERCICIO 12:
datos = [45, 12, 89, 33, 21]

print("Lista:", datos)
print("Mayor:", max(datos))
print("Menor:", min(datos))
print("Suma:", sum(datos))
print("Promedio:", sum(datos) / len(datos))
print("Cantidad de elementos:", len(datos))