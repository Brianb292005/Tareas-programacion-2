# Crud sobre dicionarios:

estudiante = {
    "nombre": "Brian",
    "edad": 20,
    "carrera": "Desarrollo de Software"
}

# Leer
print("Nombre:", estudiante["nombre"])

# Actualizar
estudiante["edad"] = 21

# Eliminar
del estudiante["carrera"]

print("Diccionario final:", estudiante)

# Eliminación de duplicados con conjuntos:

numeros = [1, 2, 3, 4, 2, 3, 5, 1]

sinduplicados = set(numeros)

print("Lista original:", numeros)
print("Sin duplicados:", sinduplicados)

# Caso práctico de modelado de datos:

curso = {
    "nombre": "Programación en Python",
    "estudiantes": ["Ana", "Luis", "Brian", "Ana"],
    "modulos": {"Variables", "Condicionales", "Bucles"}
}

print("Curso:", curso["nombre"])
print("Estudiantes inscritos:", set(curso["estudiantes"]))
print("Módulos del curso:", curso["modulos"])