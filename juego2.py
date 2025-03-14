import time
import random

# Variables globales
vidas = 100
fortuna = 0
ejercito = 0
murallas = 0

def print_pause(message):
    print(message)
    time.sleep(1.5)
import time
import random

# Variables globales
vidas = 100
fortuna = 0
ejercito = 0
murallas = 0
decidió_bayas = False  # Variable para controlar si ya se eligieron las bayas
decidió_comerciantes_mayas = False  # Variable para controlar si ya se pasó por los comerciantes mayas

def print_pause(message):
    print(message)
    time.sleep(1.5)

def mostrar_estado():
    print_pause(f"\n--- Estado actual ---")
    print_pause(f"Vida: {vidas}")
    print_pause(f"Fortuna: {fortuna}")
    print_pause(f"Ejército: {ejercito}")
    print_pause(f"Murallas: {murallas}")
    print_pause("---------------------")

def intro():
    global vidas
    print_pause("Bienvenido a 'El Ascenso del Guerrero'.")
    print_pause("Tu historia comienza en Cusco, donde tú y tus compañeros estáis esclavizados.")
    print_pause("Lográis escapar y llegáis a la ciudad portuaria de Cajamarca.")
    print_pause("Sin embargo, vuestra libertad es efímera y pronto os encontráis semi-esclavizados en Chan Chan.")
    print_pause("Decidís huir hacia la periferia, una tierra lejos del Imperio Inca.")
    print_pause("En esta tierra, debéis subsistir a base de bayas tropicales.")
    print_pause("Ves una señal con tres colores: el rojo, intocado, el azul dañado, y el negro cubierto en sangre.")
    elegir_bayas()

def elegir_bayas():
    global vidas, decidió_bayas
    if not decidió_bayas:  # Solo preguntar si no se ha decidido antes
        print_pause("\nEncuentras tres tipos de bayas:")
        print_pause("1. Bayas rojas: Sabrosas y nutritivas.")
        print_pause("2. Bayas azules: Peligrosas, pero puedes buscar un remedio.")
        print_pause("3. Bayas negras: Mortales.")

        while True:
            decision = input("¿Qué bayas eliges? (1/2/3): ")
            if decision == '1':
                print_pause("Las bayas rojas te alimentan y recuperas 20 puntos de vida.")
                vidas += 20
                break
            elif decision == '2':
                print_pause("Las bayas azules te enferman. Debes buscar una hoja de coca como remedio.")
                planta = input("Encuentras tres plantas, pero solo una es la correcta. ¿Cuál eliges? (1: Planta verde / 2: Planta roja / 3: Planta amarilla): ")
                if planta == '1':
                    print_pause("¡Correcto! Encuentras la hoja de coca y te curas.")
                    vidas += 10
                else:
                    print_pause("Esa no es la hoja de coca. Te enfermas más y pierdes 30 puntos de vida.")
                    vidas -= 30
                break
            elif decision == '3':
                print_pause("Las bayas negras son mortales. Pierdes toda tu vida.")
                vidas = 0
                break
            else:
                print_pause("Opción no válida. Por favor, elige 1, 2 o 3.")
        
        decidió_bayas = True  # Marcar que se ha tomado la decisión de las bayas
        mostrar_estado()
    
    if vidas <= 0:
        print_pause("Has muerto por comer bayas venenosas.")
        return False
    else:
        return True

def comerciantes_mayas():
    global vidas, decidió_comerciantes_mayas
    if not decidió_comerciantes_mayas:  # Solo ejecutar si no se ha pasado por los comerciantes mayas
        print_pause("\nUnos comerciantes mayas os reclutan y os llevan al Amazonas colombiano.")
        print_pause("Os trasladan a Brisbris (actual San José de Costa Rica) para ser sacrificados en un cenote.")
        print_pause("Debes convencer a los mayas de que no eres digno de ser sacrificado.")
        decision = input("¿Qué haces? (1: Persuadirlos / 2: Esperar misericordia / 3: Escapar): ")
        if decision == '1':
            print_pause("Les cuentas que en Perú tienes fortuna y que si te sacrifican, morirán.")
            print_pause("Los mayas te creen y te liberan sin daño.")
        elif decision == '2':
            print_pause("Esperas misericordia, pero los mayas deciden sacrificarte.")
            vidas = 0
        else:
            print_pause("Intentas escapar, pero los mayas te capturan y te hieren.")
            vidas = vidas // 2
        mostrar_estado()
        if vidas <= 0:
            print_pause("Has muerto en el cenote.")
            return False
        decidió_comerciantes_mayas = True  # Marcar que se ha pasado por los comerciantes mayas
    return True

# El resto de las funciones se mantienen igual...

def ruta_comercial():
    global fortuna, vidas
    print_pause("\nDe vuelta en Perú, decides comerciar en la ruta comercial maya.")
    print_pause("Debes elegir qué comerciar:")
    print_pause("1. Cacao: Ganarás mucha fortuna.")
    print_pause("2. Agua teñida de rojo: Engañas a los mayas, pero te pegarán una paliza.")
    print_pause("3. No comerciar: No ganarás fortuna y trabajarás en malas condiciones.")
    decision = input("¿Qué eliges? (1/2/3): ")
    if decision == '1':
        print_pause("Comercias con cacao y ganas 100 puntos de fortuna.")
        fortuna += 100
    elif decision == '2':
        print_pause("Engañas a los mayas con agua teñida de rojo. Ganas 50 puntos de fortuna, pero pierdes 30 de vida.")
        fortuna += 50
        vidas -= 30
    else:
        print_pause("No comercias y trabajas en malas condiciones. Pierdes 20 puntos de vida.")
        vidas -= 20
    mostrar_estado()
    if vidas <= 0:
        print_pause("Has muerto por las malas condiciones de trabajo.")
        return False
    return True

def agricultura():
    global fortuna
    print_pause("\nTe estableces en el Valle Sagrado y comienzas a trabajar en la agricultura.")
    print_pause("Debes elegir qué plantar:")
    print_pause("1. Maíz: Te harás noble rápidamente.")
    print_pause("2. Patatas: Te harás noble lentamente, pero perderás la oportunidad de cortejar a la hija del Inca.")
    print_pause("3. Tomate: Te arruinarás.")
    decision = input("¿Qué eliges? (1/2/3): ")
    if decision == '1':
        print_pause("Plantas maíz y te haces noble rápidamente. Ganas 200 puntos de fortuna.")
        fortuna += 200
    elif decision == '2':
        print_pause("Plantas patatas. Te haces noble lentamente, pero cuando quieres cortejar a la hija del Inca, ya tiene marido.")
        print_pause("Pierdes la oportunidad de ascender más.")
        return False
    else:
        print_pause("Plantas tomate y te arruinas. Pierdes toda tu fortuna.")
        fortuna = 0
    mostrar_estado()
    return True

def cortejar_inca():
    global vida, fortuna
    print_pause("\nTe mudas a Cusco y comienzas a cortejar a la hija del Inca.")
    print_pause("Ella te pone a prueba con una serie de preguntas.")
    decision = input("¿Qué haces? (1: Responder con sabiduría / 2: Responder con humor / 3: Responder con valentía): ")
    if decision == '1':
        print_pause("La hija del Inca queda impresionada por tu sabiduría y acepta tu cortejo.")
        print_pause("Te conviertes en un noble de privilegios.")
    elif decision == '2':
        print_pause("La hija del Inca se ríe de tu humor, pero no queda impresionada.")
        print_pause("Pierdes la oportunidad de ascender.")
        return False
    else:
        print_pause("La hija del Inca queda impresionada por tu valentía y te ofrece su apoyo.")
        print_pause("Te conviertes en un noble de privilegios.")
    return True

def proteger_dominios():
    global ejercito, murallas
    print_pause("\nAhora que eres un noble de privilegios, debes proteger tus dominios.")
    print_pause("Las tribus de la periferia y los españoles son una amenaza constante.")
    print_pause("Debes elegir tu estrategia:")
    print_pause("1. Atacar a las tribus periféricas: Tendrás un ejército mayor pero desorganizado.")
    print_pause("2. Reforzar murallas: Te quedarás como estás, pero no expandirás tu poder.")
    print_pause("3. Atacar a los españoles: Perderás por su superioridad táctica y armamentística.")
    decision = input("¿Qué eliges? (1/2/3): ")
    if decision == '1':
        print_pause("Atacas a las tribus periféricas y fortificas tus murallas.")
        print_pause("Los españoles son llevados a las tribus, donde tienes ventaja.")
        dado = random.randint(1, 12)
        print_pause(f"Tiras un dado y obtienes un {dado}.")
        if dado > 6:
            print_pause("¡Ganas la batalla y expandes tu poder por toda Hispanoamérica!")
        else:
            print_pause("Pierdes la batalla y tu poder se reduce.")
    elif decision == '2':
        print_pause("Refuerzas tus murallas, pero no expandes tu poder.")
    else:
        print_pause("Atacas a los españoles y pierdes por su superioridad táctica y armamentística.")
        print_pause("Tu poder se desvanece.")
    mostrar_estado()

def jugar_de_nuevo():
    decision = input("\n¿Quieres jugar de nuevo? (sí/no): ").lower()
    return decision == 'sí'

def reiniciar_juego():
    global vida, fortuna, ejercito, murallas
    vida = 100
    fortuna = 0
    ejercito = 0
    murallas = 0

def juego():
    while True:
        reiniciar_juego()
        intro()
        if elegir_bayas() and comerciantes_mayas() and ruta_comercial() and agricultura() and cortejar_inca():
            proteger_dominios()
        if not jugar_de_nuevo():
            print_pause("¡Gracias por jugar 'El Ascenso del Guerrero'! ¡Hasta la próxima!")
            break

juego()




