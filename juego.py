import time

def print_pause(message):
    print(message)
    time.sleep(1.5)

def intro():
    print_pause("Bienvenido a 'El Ascenso del Guerrero'.")
    print_pause("Tu historia comienza en Cusco, donde tú y tus compañeros estáis esclavizados.")
    print_pause("Lográis escapar y llegáis a la ciudad portuaria de Cajamarca.")
    print_pause("Sin embargo, vuestra libertad es efímera y pronto os encontráis semi-esclavizados en Chan Chan.")

def comerciante_maya():
    print_pause("\nOs encontráis con un comerciante maya que os ofrece unirse a su caravana.")
    print_pause("El comerciante os dice: 'Podéis venir con nosotros, pero el destino es incierto.'")
    decision = input("¿Aceptáis uniros a la caravana? (sí/no): ").lower()
    if decision == 'sí':
        print_pause("Os unís a la caravana y viajáis hasta Brisbris, actual San José de Costa Rica.")
        print_pause("Allí, os enfrentáis a la posibilidad de ser sacrificados en un cenote.")
        print_pause("Debéis convencer a los mayas de que no sois dignos de ser sacrificados.")
        decision = input("¿Qué hacéis? (1: Intentar convencerlos / 2: Intentar escapar): ")
        if decision == '1':
            print_pause("Lográis convencer a los mayas de que no sois dignos de ser sacrificados.")
            print_pause("Os liberan y os permiten regresar a Perú.")
            return True
        else:
            print_pause("Intentáis escapar, pero los mayas os capturan y os sacrifican.")
            return False
    else:
        print_pause("Decidís no uniros a la caravana y os quedáis en Chan Chan.")
        print_pause("Sin oportunidades, vuestra historia termina aquí.")
        return False

def noble_inca():
    print_pause("\nDe vuelta en Perú, os establecéis en el Valle Sagrado y comenzáis a trabajar en la agricultura.")
    print_pause("Un noble inca se interesa por vuestro trabajo y os ofrece su apoyo.")
    decision = input("¿Aceptáis su ayuda? (sí/no): ").lower()
    if decision == 'sí':
        print_pause("Con la ayuda del noble, vuestra fortuna crece y os convertís en un agricultor próspero.")
        return True
    else:
        print_pause("Rechazáis la ayuda del noble y vuestra situación no mejora.")
        print_pause("Vuestra historia termina aquí.")
        return False

def hija_inca():
    print_pause("\nCon vuestra nueva posición, os mudáis a Cusco y comenzáis a cortejar a la hija del Inca.")
    print_pause("La hija del Inca os pone a prueba con una serie de preguntas.")
    decision = input("¿Qué hacéis? (1: Responder con sabiduría / 2: Responder con humor / 3: Responder con valentía): ")
    if decision == '1':
        print_pause("La hija del Inca queda impresionada por vuestra sabiduría y acepta vuestro cortejo.")
        print_pause("Os convertís en un noble de privilegios y os preparáis para proteger vuestros dominios.")
        return True
    elif decision == '2':
        print_pause("La hija del Inca se ríe de vuestro humor, pero no queda impresionada.")
        print_pause("Vuestro cortejo fracasa y vuestra historia termina aquí.")
        return False
    else:
        print_pause("La hija del Inca queda impresionada por vuestra valentía y os ofrece su apoyo.")
        print_pause("Os convertís en un noble de privilegios y os preparáis para proteger vuestros dominios.")
        return True

def final():
    print_pause("\nAhora que sois un noble de privilegios, debéis proteger vuestros dominios.")
    print_pause("Las tribus de la periferia y los españoles son una amenaza constante.")
    decision = input("¿Qué hacéis? (1: Fortificar vuestras defensas / 2: Expandir vuestro territorio / 3: Buscar alianzas): ")
    if decision == '1':
        print_pause("Fortificáis vuestras defensas y lográis proteger vuestros dominios de las amenazas.")
        print_pause("Vuestra historia termina con éxito, habéis alcanzado la cima del poder.")
    elif decision == '2':
        print_pause("Intentáis expandir vuestro territorio, pero las amenazas os superan.")
        print_pause("Vuestra historia termina en fracaso.")
    else:
        print_pause("Buscáis alianzas con otras tribus y lográis fortalecer vuestra posición.")
        print_pause("Vuestra historia termina con éxito, habéis alcanzado la cima del poder.")

def jugar_de_nuevo():
    decision = input("\n¿Quieres jugar de nuevo? (sí/no): ").lower()
    return decision == 'sí'

def juego():
    while True:
        intro()
        if comerciante_maya():
            if noble_inca():
                if hija_inca():
                    final()
        if not jugar_de_nuevo():
            print_pause("¡Gracias por jugar 'El Ascenso del Guerrero'! ¡Hasta la próxima!")
            break

juego()
