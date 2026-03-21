# Ejercicios seleccionados:

# Depuración

# Un programa donde una variable cambie varias veces y ellos deban seguir su valor paso a paso:
    
    # ================================================
# DEPURACIÓN: Seguimiento de una variable paso a paso
# ================================================

print("DEBUG - Inicio del programa")
total = 0
print(f"DEBUG - total inicial: {total}")

# Paso 1: Se asigna un valor base
total = 10
print(f"DEBUG - Paso 1 | total después de asignar valor base: {total}")

# Paso 2: Se le suma una cantidad
total = total + 25
print(f"DEBUG - Paso 2 | total después de sumar 25: {total}")

# Paso 3: Se multiplica por un factor
total = total * 2
print(f"DEBUG - Paso 3 | total después de multiplicar por 2: {total}")

# Paso 4: Se le resta un descuento
descuento = 15
total = total - descuento
print(f"DEBUG - Paso 4 | total después de restar descuento ({descuento}): {total}")

# Paso 5: Se divide entre número de personas
personas = 3
total = total / personas
print(f"DEBUG - Paso 5 | total después de dividir entre {personas} personas: {total:.2f}")

print("\n✅ RESULTADO FINAL:", round(total, 2))
print("DEBUG - Fin del programa")

# Ejercicio 2 de Depuración — Validar divisor cero:

# ================================================
# DEPURACIÓN: Validación antes de dividir
# ================================================

print("DEBUG - Inicio del programa de división")

# Solicitar datos al usuario
dividendo = float(input("Ingrese el número a dividir (dividendo): "))
print(f"DEBUG - Dividendo recibido: {dividendo}")

divisor = float(input("Ingrese el número por el que va a dividir (divisor): "))
print(f"DEBUG - Divisor recibido: {divisor}")

# Validación ANTES de intentar dividir
print("DEBUG - Iniciando validación del divisor...")

if divisor == 0:
    print("DEBUG - ¡ALERTA! El divisor es cero, operación cancelada.")
    print("❌ Error: No es posible dividir entre cero.")
else:
    print("DEBUG - Validación superada, procediendo con la división...")
    resultado = dividendo / divisor
    print(f"DEBUG - Operación realizada: {dividendo} / {divisor}")
    print(f"\n✅ Resultado: {dividendo} / {divisor} = {resultado:.2f}")

print("DEBUG - Fin del programa")

# Ejercicio 2 de Módulos — Validar edad y mostrar mensaje

# ================================================
# MÓDULOS: Función que valida edad y otra que muestra mensaje
# ================================================

# --- FUNCIÓN 1: Solo valida la edad ---
def validar_edad(edad):
    print(f"DEBUG - Validando edad: {edad}")

    if not isinstance(edad, int):
        return "error_tipo"
    elif edad < 0:
        return "error_negativo"
    elif edad < 18:
        return "menor"
    elif edad <= 64:
        return "adulto"
    else:
        return "adulto_mayor"


# --- FUNCIÓN 2: Solo muestra el mensaje según el resultado ---

def mostrar_mensaje(resultado, nombre):
    print(f"DEBUG - Resultado recibido por mostrar_mensaje: {resultado}")

    if resultado == "error_tipo":
        print(f"❌ Error: La edad de {nombre} no es un número entero válido.")
    elif resultado == "error_negativo":
        print(f"❌ Error: La edad de {nombre} no puede ser negativa.")
    elif resultado == "menor":
        print(f"⚠️  Hola {nombre}, eres menor de edad. Acceso restringido.")
    elif resultado == "adulto":
        print(f"✅ Bienvenido/a {nombre}, eres mayor de edad. Acceso permitido.")
    elif resultado == "adulto_mayor":
        print(f"🌟 Bienvenido/a {nombre}, acceso permitido con beneficios especiales.")


# --- PROGRAMA PRINCIPAL ---
print("=== Sistema de verificación de edad ===\n")

nombre = input("Ingrese su nombre: ")
print(f"DEBUG - Nombre recibido: {nombre}")

try:
    edad = int(input("Ingrese su edad: "))
except ValueError:
    edad = "invalido"

resultado = validar_edad(edad)
mostrar_mensaje(resultado, nombre)

print("\nDEBUG - Programa finalizado correctamente.")


# Ejercicio 3 de Módulos — Funciones organizadas por bloques: Entrada, Proceso y Salida:

# ================================================
# MÓDULOS: Programa organizado en bloques
# entrada → proceso → salida
# ================================================

# ============ BLOQUE 1: ENTRADA ============
def pedir_estudiante():
    """Recoge todos los datos del estudiante."""
    print("DEBUG - Bloque ENTRADA iniciado")

    nombre = input("Ingrese su nombre completo: ").strip()
    print(f"DEBUG - Nombre recibido: {nombre}")

    carrera = input("Ingrese su carrera: ").strip()
    print(f"DEBUG - Carrera recibida: {carrera}")

    try:
        nota1 = float(input("Ingrese la nota 1 (0-100): "))
        nota2 = float(input("Ingrese la nota 2 (0-100): "))
        nota3 = float(input("Ingrese la nota 3 (0-100): "))
    except ValueError:
        print("❌ Error: Las notas deben ser números.")
        return None

    print("DEBUG - Bloque ENTRADA finalizado\n")
    return {
        "nombre":  nombre,
        "carrera": carrera,
        "notas":   [nota1, nota2, nota3]
    }


# ============ BLOQUE 2: PROCESO ============
def procesar_estudiante(datos):
    """Realiza todos los cálculos sobre los datos recibidos."""
    print("DEBUG - Bloque PROCESO iniciado")

    notas   = datos["notas"]
    promedio = sum(notas) / len(notas)
    print(f"DEBUG - Promedio calculado: {promedio:.2f}")

    nota_mayor = max(notas)
    nota_menor = min(notas)
    print(f"DEBUG - Mayor: {nota_mayor} | Menor: {nota_menor}")

    if promedio >= 90:
        estado = "Excelente 🏆"
    elif promedio >= 70:
        estado = "Aprobado ✅"
    elif promedio >= 60:
        estado = "En riesgo ⚠️"
    else:
        estado = "Reprobado ❌"

    print(f"DEBUG - Estado asignado: {estado}")
    print("DEBUG - Bloque PROCESO finalizado\n")

    return {
        "promedio":    round(promedio, 2),
        "nota_mayor":  nota_mayor,
        "nota_menor":  nota_menor,
        "estado":      estado
    }

# ============ BLOQUE 3: SALIDA ============
def mostrar_resultado(datos, resultados):
    """Muestra el reporte final al usuario."""
    print("DEBUG - Bloque SALIDA iniciado")
    print("\n" + "=" * 45)
    print("         📋 REPORTE DEL ESTUDIANTE")
    print("=" * 45)
    print(f"  Nombre   : {datos['nombre']}")
    print(f"  Carrera  : {datos['carrera']}")
    print(f"  Notas    : {datos['notas']}")
    print("-" * 45)
    print(f"  Promedio : {resultados['promedio']}")
    print(f"  Mayor    : {resultados['nota_mayor']}")
    print(f"  Menor    : {resultados['nota_menor']}")
    print(f"  Estado   : {resultados['estado']}")
    print("=" * 45)
    print("DEBUG - Bloque SALIDA finalizado")


# ============ PROGRAMA PRINCIPAL ============
print("=== Sistema de evaluación estudiantil ===\n")

datos = pedir_estudiante()

if datos is not None:
    resultados = procesar_estudiante(datos)
    mostrar_resultado(datos, resultados)
else:
    print("⚠️ El programa terminó por datos inválidos.")