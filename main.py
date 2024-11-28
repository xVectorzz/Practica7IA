import re

def llenar_ranuras(oracion):
    # Patrones mejorados para identificar las ranuras
    patron_origen = r'\b(?:de|desde)\s([\w\s]+?)\b(?:a|hacia)\b'
    patron_destino = r'\b(?:a|hacia)\s([\w\s]+?)\b(?:el|para|en|el|la)\b'
    patron_fecha = r'\b(?:el|para|en)\s([\d]{1,2}\sde\s\w+|\d{1,2}/\d{1,2}/\d{4}|\d{1,2}-\d{1,2}-\d{4})'

    # Buscar coincidencias en la oración
    match_origen = re.search(patron_origen, oracion)
    match_destino = re.search(patron_destino, oracion)
    match_fecha = re.search(patron_fecha, oracion)

    # Extraer valores
    origen = match_origen.group(1).strip() if match_origen else 'No encontrado'
    destino = match_destino.group(1).strip() if match_destino else 'No encontrado'
    fecha = match_fecha.group(1).strip() if match_fecha else 'No encontrado'

    # Retornar los resultados como un diccionario
    return {
        'Origen': origen,
        'Destino': destino,
        'Fecha': fecha
    }

def mostrar_descripcion():
    print("\nDescripción del programa:")
    print("Este programa permite identificar tres elementos clave en frases relacionadas con reservas de viajes:")
    print("- Origen: El lugar desde donde se inicia el viaje.")
    print("- Destino: El lugar al que se quiere viajar.")
    print("- Fecha: La fecha del viaje, en formatos como '10 de diciembre', '10/12/2024' o '10-12-2024'.")
    print("\nIngrese una frase como: 'Reserva un vuelo de Madrid a Londres el 10 de diciembre' para probarlo.")

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Ejecutar el programa")
        print("2. Descripción del programa")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            oracion = input("\nIngrese una frase para procesar: ")
            ranuras = llenar_ranuras(oracion)
            print(f"\nResultado:")
            print(f"Origen: {ranuras['Origen']}")
            print(f"Destino: {ranuras['Destino']}")
            print(f"Fecha: {ranuras['Fecha']}")
        elif opcion == '2':
            mostrar_descripcion()
        elif opcion == '3':
            print("Saliendo del programa. ¡Gracias por usarlo!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

# Ejecutar el menú
menu()
