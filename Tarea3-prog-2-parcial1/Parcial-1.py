print("Bienvenidos a VitalForge - Tu tienda de confianza para suplementos de salud y bienestar en línea.")

edad = int(input("Por favor, ingresa tu edad: "))

if edad < 18:
    print("Lo siento, debes ser mayor de edad para realizar compras en VitalForge.")
else:
    print("¡Gracias por ingresar tu edad! Ahora puedes explorar nuestra amplia gama de suplementos de salud y bienestar.")
    
    Registro = input("¿Deseas registrarte para recibir ofertas exclusivas? si/no: ")
    
    si = "si"

    while Registro == si:
        
      correo = input("Por favor, ingresa tu correo electrónico: ")
      nombre = input("Por favor, ingresa tu nombre: ")
      apellidos = input("Por favor, ingresa tus apellidos: ")
    
      print("¡Gracias por registrarte! Ahora recibirás ofertas exclusivas y novedades sobre nuestros productos.")
      
    if Registro == "no":
        
        print("No hay problema. Puedes seguir explorando nuestra tienda sin registrarte.")
         
    Ver_productos = input("¿Deseas ver los productos disponibles? si/no: ")
    
    if Ver_productos == "si":
        print("¡Genial! Aquí tienes una lista de nuestros productos disponibles:")
        print("- Proteína en polvo")
        print("- Vitaminas y minerales")
        print("- Suplementos para el rendimiento deportivo")
        print("- Productos para la salud digestiva")
        
    else: 
        if Ver_productos == "no":
            print(" Aquí tienes una lista de nuestros productos disponibles:")
        print("- Proteína en polvo")
        print("- Vitaminas y minerales")
        print("- Suplementos para el rendimiento deportivo")
        print("- Productos para la salud digestiva")
    
    