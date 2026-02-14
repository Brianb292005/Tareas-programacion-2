def verificar_edad():
    """Verificar si el cliente es mayor de edad"""
    print("Bienvenidos a Brianfitness - Tu tienda de confianza para suplementos de salud y bienestar en línea.")
    edad = int(input("\nPor favor, ingresa tu edad: "))
    
    if edad < 18:
        print("Lo siento, debes ser mayor de edad para realizar compras en Brianfitness.")
        return None
    else:
        print("¡Gracias por ingresar tu edad! Ahora puedes explorar nuestra amplia gama de suplementos de salud y bienestar.")
        return edad
    
def registrar_cliente():
    """Registrar o pedir datos básicos del cliente"""
    registro = input("\n¿Deseas registrarte para recibir ofertas exclusivas? si/no: ").lower()
    
    if registro == "si":
        correo = input("Por favor, ingresa tu correo electrónico: ")
        nombre = input("Por favor, ingresa tu nombre: ")
        apellidos = input("Por favor, ingresa tus apellidos: ")
        print("¡Gracias por registrarte! Ahora recibirás ofertas exclusivas y novedades sobre nuestros productos.")
    else:
        correo = ""
        nombre = input("Por favor, ingresa tu nombre para continuar: ")
        apellidos = ""
        print("No hay problema. Puedes seguir explorando nuestra tienda sin registrarte.")
    
    return correo, nombre, apellidos


def mostrar_catalogo():
    """Mostrar el catálogo de productos disponibles"""
    ver_productos = input("¿Deseas ver los productos disponibles? si/no: ").lower()
    
    if ver_productos == "si":
        print("¡Genial! Aquí tienes una lista de nuestros productos disponibles:")
    else:
        print("\nDe acuerdo, si cambias de opinión, aquí está el catálogo:")
    
    # Diccionario con productos y precios
    productos = {
        "1": {"nombre": "Proteína Whey", "precio": 1500.00},
        "2": {"nombre": "Creatina Monohidratada", "precio": 800.00},
        "3": {"nombre": "Pre-Workout", "precio": 1200.00},
        "4": {"nombre": "BCAAs", "precio": 900.00},
        "5": {"nombre": "Multivitamínico", "precio": 600.00},
        "6": {"nombre": "Omega 3", "precio": 700.00},
        "7": {"nombre": "Quemador de Grasa", "precio": 1400.00},
        "8": {"nombre": "Ganador de Peso", "precio": 2000.00}
    }
    
    print("\n" + "="*60)
    print("CATÁLOGO DE PRODUCTOS")
    print("="*60)
    for key, producto in productos.items():
        print(f"{key}. {producto['nombre']} - ${producto['precio']:.2f}")
    print("="*60)
    
    return productos


def realizar_compra(productos):
    """Procesar la compra de productos y retornar el carrito"""
    carrito = []
    total_items = 0
    seguir_comprando = "si"
    
    while seguir_comprando == "si":
        producto_id = input("¿Qué producto deseas comprar? (ingresa el número): ")
        
        if producto_id in productos:
            cantidad = int(input(f"¿Cuántas unidades de {productos[producto_id]['nombre']} deseas? "))
            
            # Agregar al carrito
            carrito.append({
                "nombre": productos[producto_id]['nombre'],
                "precio": productos[producto_id]['precio'],
                "cantidad": cantidad,
                "subtotal": productos[producto_id]['precio'] * cantidad
            })
            
            total_items += cantidad
            print(f"✓ {cantidad} x {productos[producto_id]['nombre']} agregado(s) al carrito.")
            
        else:
            print("Producto no válido. Por favor elige un número del 1 al 8.")
            continue
        
        seguir_comprando = input("¿Deseas agregar otro producto? si/no: ").lower()
    
    return carrito, total_items


def calcular_totales(carrito):
    """Calcular subtotal, aplicar descuento si corresponde y retornar totales"""
    subtotal_total = 0
    
    # Sumar todos los subtotales del carrito
    for item in carrito:
        subtotal_total += item['subtotal']
    
    # Aplicar descuento del 10% si el subtotal es mayor a 5000
    if subtotal_total > 5000:
        descuento = subtotal_total * 0.10
        total_final = subtotal_total - descuento
        tiene_descuento = True
    else:
        descuento = 0
        total_final = subtotal_total
        tiene_descuento = False
    
    return subtotal_total, descuento, total_final, tiene_descuento


def clasificar_cliente(edad):
    """Clasificar al cliente según su edad"""
    if edad < 18:
        return "Cliente menor de edad"
    elif 18 <= edad <= 59:
        return "Cliente adulto"
    else:
        return "Cliente adulto mayor"


def mostrar_ticket(nombre, apellidos, edad, carrito, total_items, subtotal_total, descuento, total_final, tiene_descuento):
    """Mostrar el ticket final de compra"""
    print("" + "="*60)
    print("RESUMEN DE TU COMPRA")
    print("="*60)
    
    print("Productos en tu carrito:")
    for item in carrito:
        print(f"  • {item['cantidad']} x {item['nombre']} - ${item['precio']:.2f} c/u = ${item['subtotal']:.2f}")
    
    print(f"Subtotal: ${subtotal_total:.2f}")
    
    if tiene_descuento:
        print(f"Descuento (10%): -${descuento:.2f}")
    
    print(f"TOTAL A PAGAR: ${total_final:.2f}")
    
    # Clasificación del cliente
    clasificacion = clasificar_cliente(edad)
    
    # Ticket final
    print("" + "="*60)
    print("TICKET DE COMPRA - Brianfitness")
    print("="*60)
    print(f"Cliente: {nombre.upper()} {apellidos.upper()}")
    print(f"Edad: {edad} años")
    print(f"Clasificación: {clasificacion}")
    print(f"Total de productos: {total_items}")
    print(f"Total a pagar: ${total_final:.2f}")
    print("="*60)
    print("¡Gracias por tu compra en Brianfitness!")
    print("Tu pedido será procesado y enviado pronto.")
    print("="*60)


def main():
    """Función principal que ejecuta todo el programa"""
    # Verificar edad
    edad = verificar_edad()
    if edad is None:
        return  # Salir si es menor de edad
    
    # Registrar cliente
    correo, nombre, apellidos = registrar_cliente()
    
    # Mostrar catálogo
    productos = mostrar_catalogo()
    
    # Realizar compra
    carrito, total_items = realizar_compra(productos)
    
    # Calcular totales
    subtotal_total, descuento, total_final, tiene_descuento = calcular_totales(carrito)
    
    # Mostrar ticket
    mostrar_ticket(nombre, apellidos, edad, carrito, total_items, 
                   subtotal_total, descuento, total_final, tiene_descuento)


# Ejecutar el programa
if __name__ == "__main__":
    main()