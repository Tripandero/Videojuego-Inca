import random
import time

class GameState:
    def __init__(self):
        self.vida = 100
        self.fortuna = 0
        self.ejercito = 0
        self.murallas = 0
    
    def mostrar_estado(self):
        print(f"\n--- Estado actual ---")
        print(f"Vida: {self.vida}")
        print(f"Fortuna: {self.fortuna}")
        print(f"Ejército: {self.ejercito}")
        print(f"Murallas: {self.murallas}")
        print("---------------------")
        time.sleep(1.5)

class Personaje:
    def __init__(self, nombre, vida, daño_base):
        self.nombre = nombre
        self.vida = vida
        self.daño_base = daño_base
    
    def atacar(self, enemigo, tipo_ataque):
        if tipo_ataque == "básico":
            daño = self.daño_base
        elif tipo_ataque == "especial":
            daño = 50
        else:
            print("Tipo de ataque no reconocido")
            return

        enemigo.vida -= daño
        print(f"{self.nombre} atacó a {enemigo.nombre} causando {daño} de daño.")
    
    def recibir_daño(self, daño):
        self.vida -= daño
        print(f"{self.nombre} ha recibido {daño} de daño.")
    
    def esta_vivo(self):
        return self.vida > 0
    
    def mostrar_estado(self):
        print(f"{self.nombre} - Vida: {self.vida}")

class Batalla:
    @staticmethod
    def ejecutar(jugador_vida=300, enemigo_vida=80):
        jugador = Personaje("Jugador", jugador_vida, 10)
        enemigo = Personaje("Enemigo", enemigo_vida, 20)
        especial_usado = False

        while jugador.esta_vivo() and enemigo.esta_vivo():
            jugador.mostrar_estado()
            enemigo.mostrar_estado()

            print("\n1. Ataque Básico (10 de daño)")
            if not especial_usado:
                print("2. Ataque Especial (50 de daño)")
            else:
                print("2. Escapar")

            tipo_ataque = input("Selecciona una opción (1 o 2): ").strip()

            if tipo_ataque == "1":
                jugador.atacar(enemigo, "básico")
            elif tipo_ataque == "2" and not especial_usado:
                jugador.atacar(enemigo, "especial")
                especial_usado = True
            elif tipo_ataque == "2" and especial_usado:
                print("\nHas decidido escapar de la batalla.")
                break
            else:
                print("Opción no válida. Se usará ataque básico por defecto.")
                jugador.atacar(enemigo, "básico")

            if not enemigo.esta_vivo():
                print("\n¡Has derrotado al enemigo!")
                break

            if enemigo.esta_vivo():
                enemigo.atacar(jugador, "básico")
                if not jugador.esta_vivo():
                    print("\n¡El enemigo te ha derrotado!")
                    break

            time.sleep(1)

        print("\n¡Batalla terminada!")
        return jugador.esta_vivo()

class ModoHistoria:
    def __init__(self):
        self.estado = GameState()
    
    def print_pause(self, message):
        print(message)
        time.sleep(1.5)
    
    def intro(self):
        self.print_pause("Bienvenido a 'El Ascenso del Guerrero'.")
        self.print_pause("Tu historia comienza en Cusco, donde tú y tus compañeros estáis esclavizados.")
        self.print_pause("Lográis escapar y llegáis a la ciudad portuaria de Cajamarca.")
        self.print_pause("Sin embargo, vuestra libertad es efímera y pronto os encontráis semi-esclavizados en Chan Chan.")
        self.print_pause("Decidís huir hacia la periferia, una tierra lejos del Imperio Inca.")
        self.print_pause("En esta tierra, debéis subsistir a base de bayas tropicales.")
        self.print_pause("Encuentras una señal con tres colores, el rojo limpio, el azul sucio, y el negro cubierto en sangre.")
    
    def elegir_bayas(self):
        self.print_pause("\nEncuentras tres tipos de bayas:")
        self.print_pause("1. Bayas rojas")
        self.print_pause("2. Bayas azules")
        self.print_pause("3. Bayas negras")
        decision = input("¿Qué bayas eliges? (1/2/3): ")
        if decision == '1':
            self.print_pause("Las bayas rojas te alimentan y recuperas 20 puntos de vida.")
            self.estado.vida += 20
        elif decision == '2':
            self.print_pause("Las bayas azules te enferman. Debes buscar una hoja de coca como remedio.")
            self.print_pause("Encuentras tres plantas, pero solo una es la correcta.")
            planta = input("¿Cuál eliges? (1: Planta negra / 2: Planta roja / 3: Planta azul): ")
            if planta == '2':
                self.print_pause("¡Correcto! Encuentras la hoja de coca y te curas.")
                self.estado.vida += 10
            else:
                self.print_pause("Esa no es la hoja de coca. Te enfermas más y pierdes 30 puntos de vida.")
                self.estado.vida -= 30
        else:
            self.print_pause("Las bayas negras son mortales. Pierdes toda tu vida.")
            self.estado.vida = 0
        self.estado.mostrar_estado()
        return self.estado.vida > 0
    
    def ejecutar(self):
        self.estado = GameState()
        self.intro()
        
        if (self.elegir_bayas() and Batalla.ejecutar() and 
            self.comerciantes_mayas() and Batalla.ejecutar() and 
            self.ruta_comercial() and Batalla.ejecutar() and 
            self.agricultura() and Batalla.ejecutar() and 
            self.cortejar_inca() and Batalla.ejecutar()):
            self.proteger_dominios()
    
    def comerciantes_mayas(self):
        self.print_pause("\nUnos comerciantes mayas os reclutan y os llevan al Amazonas colombiano.")
        self.print_pause("Os trasladan a Brisbris (actual San José de Costa Rica) para ser sacrificados en un cenote.")
        self.print_pause("Debes convencer a los mayas de que no eres digno de ser sacrificado.")
        decision = input("¿Qué haces? (1: Persuadirlos / 2: Esperar misericordia / 3: Escapar): ")
        if decision == '1':
            self.print_pause("Les cuentas que en Perú tienes fortuna y que si te sacrifican, morirán.")
            self.print_pause("Los mayas te creen y te liberan sin daño.")
        elif decision == '2':
            self.print_pause("Esperas misericordia, pero los mayas deciden sacrificarte.")
            self.estado.vida = 0
        else:
            self.print_pause("Intentas escapar, pero los mayas te capturan y te hieren.")
            self.estado.vida = self.estado.vida // 2
        self.estado.mostrar_estado()
        return self.estado.vida > 0
    
    def ruta_comercial(self):
        self.print_pause("\nDe vuelta en Perú, decides comerciar en la ruta comercial maya.")
        self.print_pause("Debes elegir qué comerciar:")
        self.print_pause("1. Cacao")
        self.print_pause("2. Agua teñida de rojo")
        self.print_pause("3. No comerciar")
        decision = input("¿Qué eliges? (1/2/3): ")
        if decision == '1':
            self.print_pause("Comercias con cacao y ganas 100 puntos de fortuna.")
            self.estado.fortuna += 100
        elif decision == '2':
            self.print_pause("Engañas a los mayas con agua teñida de rojo. Ganas 50 puntos de fortuna, pero pierdes 30 de vida.")
            self.estado.fortuna += 50
            self.estado.vida -= 30
        else:
            self.print_pause("No comercias y trabajas en malas condiciones. Pierdes 20 puntos de vida.")
            self.estado.vida -= 20
        self.estado.mostrar_estado()
        return self.estado.vida > 0
    
    def agricultura(self):
        self.print_pause("\nTe estableces en el Valle Sagrado y comienzas a trabajar en la agricultura.")
        self.print_pause("Debes elegir qué plantar:")
        self.print_pause("1. Maíz")
        self.print_pause("2. Patatas")
        self.print_pause("3. Tomate")
        decision = input("¿Qué eliges? (1/2/3): ")
        if decision == '1':
            self.print_pause("Plantas maíz y te haces noble rápidamente. Ganas 200 puntos de fortuna.")
            self.estado.fortuna += 200
        elif decision == '2':
            self.print_pause("Plantas patatas. Te haces noble lentamente, pero cuando quieres cortejar a la hija del Inca, ya tiene marido.")
            self.print_pause("Pierdes la oportunidad de ascender más.")
            return False
        else:
            self.print_pause("Plantas tomate y te arruinas. Pierdes toda tu fortuna.")
            self.estado.fortuna = 0
        self.estado.mostrar_estado()
        return True
    
    def cortejar_inca(self):
        self.print_pause("\nTe mudas a Cusco y comienzas a cortejar a la hija del Inca.")
        self.print_pause("Ella te pone a prueba con una serie de preguntas.")
        decision = input("¿Qué haces? (1: Responder con sabiduría / 2: Responder con humor / 3: Responder con valentía): ")
        if decision == '1':
            self.print_pause("La hija del Inca queda impresionada por tu sabiduría y acepta tu cortejo.")
            self.print_pause("Te conviertes en un noble de privilegios.")
        elif decision == '2':
            self.print_pause("La hija del Inca se ríe de tu humor, pero no queda impresionada.")
            self.print_pause("Pierdes la oportunidad de ascender.")
            return False
        else:
            self.print_pause("La hija del Inca queda impresionada por tu valentía y te ofrece su apoyo.")
            self.print_pause("Te conviertes en un noble de privilegios.")
        return True
    
    def proteger_dominios(self):
        self.print_pause("\nAhora que eres un noble de privilegios, debes proteger tus dominios.")
        self.print_pause("Las tribus de la periferia y los españoles son una amenaza constante.")
        self.print_pause("Debes elegir tu estrategia:")
        self.print_pause("1. Atacar a las tribus periféricas: Tendrás un ejército mayor pero desorganizado.")
        self.print_pause("2. Reforzar murallas: Te quedarás como estás, pero no expandirás tu poder.")
        self.print_pause("3. Atacar a los españoles: Perderás por su superioridad táctica y armamentística.")
        decision = input("¿Qué eliges? (1/2/3): ")
        if decision == '1':
            self.print_pause("Atacas a las tribus periféricas y fortificas tus murallas.")
            self.print_pause("Los españoles son llevados a las tribus, donde tienes ventaja.")
            dado = random.randint(1, 12)
            self.print_pause(f"Tiras un dado y obtienes un {dado}.")
            if dado > 6:
                self.print_pause("¡Ganas la batalla y expandes tu poder por toda Hispanoamérica!")
            else:
                self.print_pause("Pierdes la batalla y tu poder se reduce.")
        elif decision == '2':
            self.print_pause("Refuerzas tus murallas, pero no expandes tu poder.")
        else:
            self.print_pause("Atacas a los españoles y pierdes por su superioridad táctica y armamentística.")
            self.print_pause("Tu poder se desvanece.")
        self.estado.mostrar_estado()

class ModoBatalla:
    class PersonajeBatalla:
        def __init__(self, nombre, significado, tipo, vida, ataque, velocidad, alcance, especial, armas):
            self.nombre = nombre
            self.significado = significado
            self.tipo = tipo
            self.vida_max = vida
            self.vida = vida
            self.ataque = ataque
            self.velocidad = velocidad
            self.alcance = alcance
            self.especial = especial
            self.armas = armas
            self.arma_actual = armas[0]
            self.especial_disponible = True
            self.defensa_activada = False
        
        def mostrar_info_detallada(self):
            print(f"\n=== {self.nombre} ===")
            print(f"Significado: {self.significado}")
            print(f"Tipo: {self.tipo}")
            print(f"Vida: {self.vida}/{self.vida_max}")
            print(f"Ataque: {self.ataque}")
            print(f"Velocidad: {self.velocidad}")
            print(f"Alcance: {self.alcance}")
            print(f"Habilidad especial: {self.especial}")
            print(f"Arma actual: {self.arma_actual}")
            print("\nArmas disponibles:")
            for i, arma in enumerate(self.armas, 1):
                print(f"{i}. {arma}")
        
        def cambiar_arma(self):
            print("\nArmas disponibles:")
            for i, arma in enumerate(self.armas, 1):
                print(f"{i}. {arma}")
            try:
                opcion = int(input("Elige un arma (número): ")) - 1
                if 0 <= opcion < len(self.armas):
                    self.arma_actual = self.armas[opcion]
                    print(f"\n¡Has equipado {self.arma_actual}!")
                    return True
                else:
                    print("Opción inválida. No cambias de arma.")
                    return False
            except ValueError:
                print("Entrada inválida. No cambias de arma.")
                return False
        
        def usar_especial(self, objetivo=None):
            if not self.especial_disponible:
                print("\n¡Habilidad especial no disponible!")
                return False

            self.especial_disponible = False
            if self.nombre == "Aymara":
                danio = 300
                objetivo.vida -= danio
                print(f"\n¡{self.nombre} usa Rompetierras y hace {danio} de daño a {objetivo.nombre}!")
                print(f"¡{objetivo.nombre} queda paralizado por un turno!")
                return "paralizado"
            elif self.nombre == "Suhay":
                danio = 50
                objetivo.vida -= danio
                print(f"\n¡{self.nombre} usa Maíz caliente y hace {danio} de daño a {objetivo.nombre}!")
            elif self.nombre == "Wayna":
                danio = 100
                objetivo.vida -= danio
                print(f"\n¡{self.nombre} usa Cuchilla Venenosa y hace {danio} de daño a {objetivo.nombre}!")
                print(f"¡{objetivo.nombre} seguirá recibiendo daño por veneno!")
                return "envenenado"
            elif self.nombre == "Koka":
                curacion = min(100, self.vida_max - self.vida)
                self.vida += curacion
                print(f"\n¡{self.nombre} usa Puré de coca y recupera {curacion} de vida!")
            return None
        
        def defender(self):
            self.defensa_activada = True
            print(f"\n¡{self.nombre} se prepara para defenderse!")
            return True
    
    class NPC(PersonajeBatalla):
        def __init__(self, nombre, significado, tipo, vida, ataque, velocidad, alcance, especial, armas, personalidad):
            super().__init__(nombre, significado, tipo, vida, ataque, velocidad, alcance, especial, armas)
            self.personalidad = personalidad
            self.frases = {
                "agresivo": [
                    "¡Te aplastaré como a un insecto!",
                    "¡No tienes oportunidad contra mí!",
                    "¡Prepárate para sufrir!",
                    "¡Esta batalla terminará con tu derrota!"
                ],
                "defensivo": [
                    "¡No podrás pasarme!",
                    "¡Mi defensa es impenetrable!",
                    "¡Ataca si te atreves!",
                    "¡Protegeré mi posición!"
                ],
                "astuto": [
                    "¡Ja! ¿En serio crees que puedes ganar?",
                    "¡Mis movimientos son impredecibles!",
                    "¡Caerás en mi trampa!",
                    "¡La astucia vence a la fuerza bruta!"
                ]
            }
        
        def hablar(self):
            frase = random.choice(self.frases[self.personalidad])
            print(f"\n{self.nombre}: {frase}")
        
        def decidir_accion(self, jugador):
            self.hablar()
            time.sleep(1)
            
            if self.vida < self.vida_max * 0.3 and random.random() < 0.7:
                return "defender"
            elif self.especial_disponible and random.random() < 0.6:
                return "especial"
            elif random.random() < 0.3:
                return "cambiar_arma"
            else:
                return "atacar"
    
    def __init__(self):
        self.personajes = {
            "Aymara": self.PersonajeBatalla(
                nombre="Aymara",
                significado="Significa ser fuerte y trabajador",
                tipo="Tanque",
                vida=500,
                ataque=100,
                velocidad=10,
                alcance=10,
                especial="Rompetierras: hace 300 de daño y deja paralizado al enemigo por un turno",
                armas=["Puños (inicial)", "Tuccina", "Chaska", "Porra", "Sable"]
            ),
            "Suhay": self.PersonajeBatalla(
                nombre="Suhay",
                significado="El que es tal como el maíz amarillo, abundante y fino. Roca y peña",
                tipo="Alcance",
                vida=150,
                ataque=100,
                velocidad=50,
                alcance=100,
                especial="Maíz caliente: causa 50 de daño a todos los enemigos",
                armas=["Manos (inicial)", "Tirachinas", "Cerbatana", "Honda", "Arco y Flecha"]
            ),
            "Wayna": self.PersonajeBatalla(
                nombre="Wayna",
                significado="Mozo, joven, buen amigo",
                tipo="Ágil",
                vida=120,
                ataque=120,
                velocidad=150,
                alcance=30,
                especial="Cuchilla Venenosa: causa 100 de daño cada turno a un enemigo",
                armas=["Manos (inicial)", "Hoz Sicán", "Cunca", "Cimitarra", "Cuchillo de doble filo"]
            ),
            "Koka": self.PersonajeBatalla(
                nombre="Koka",
                significado="Coca, planta sagrada",
                tipo="Espadachina",
                vida=200,
                ataque=150,
                velocidad=80,
                alcance=50,
                especial="Puré de coca: cura 100 de vida",
                armas=["Palo largo (inicial)", "Jabalina", "Guja", "Antañauichi", "Alabardas"]
            )
        }
    
    def mostrar_personajes(self):
        print("\n=== PERSONAJES DISPONIBLES ===")
        for personaje in self.personajes.values():
            personaje.mostrar_info_detallada()
            print("\n" + "="*50 + "\n")
    
    def elegir_personaje(self):
        self.mostrar_personajes()
        print("\nElige tu personaje:")
        for nombre in self.personajes.keys():
            print(f"- {nombre}")
        
        while True:
            eleccion = input("\n¿Qué personaje deseas jugar? ").capitalize()
            if eleccion in self.personajes:
                return self.personajes[eleccion]
            else:
                print("Personaje no válido. Por favor, elige uno de los listados.")
    
    def crear_enemigo(self):
        enemigos = [
            self.NPC(
                nombre="Tupac",
                significado="El rebelde",
                tipo="Guerrero",
                vida=250,
                ataque=80,
                velocidad=60,
                alcance=40,
                especial="Grito de guerra: aumenta su ataque en 50% por 2 turnos",
                armas=["Garrote", "Hacha", "Maza"],
                personalidad="agresivo"
            ),
            self.NPC(
                nombre="Mama Ocllo",
                significado="La sabia",
                tipo="Hechicera",
                vida=180,
                ataque=60,
                velocidad=70,
                alcance=80,
                especial="Barrera mágica: reduce el daño recibido en 75% por 1 turno",
                armas=["Báculo", "Orbe", "Daga ceremonial"],
                personalidad="defensivo"
            ),
            self.NPC(
                nombre="Atahualpa",
                significado="El estratega",
                tipo="Táctico",
                vida=220,
                ataque=70,
                velocidad=90,
                alcance=60,
                especial="Trampa dorada: reduce la velocidad del enemigo a la mitad por 2 turnos",
                armas=["Lanza", "Espada curva", "Honda especial"],
                personalidad="astuto"
            )
        ]
        return random.choice(enemigos)
    
    def aplicar_efectos(self, jugador, enemigo, efectos):
        nuevos_efectos = {}
        
        for personaje, efecto in efectos.items():
            if efecto == "paralizado":
                print(f"\n¡{personaje.nombre} está paralizado y no puede moverse!")
                nuevos_efectos[personaje] = None
            elif efecto == "envenenado":
                danio = 30
                personaje.vida -= danio
                print(f"\n¡{personaje.nombre} sufre {danio} de daño por veneno!")
                if random.random() < 0.5:
                    nuevos_efectos[personaje] = "envenenado"
        
        return nuevos_efectos
    
    def batalla(self, jugador, enemigo):
        print(f"\n¡Un {enemigo.tipo.lower()} llamado {enemigo.nombre} aparece frente a ti!")
        print(f"{enemigo.nombre}: \"{random.choice(enemigo.frases[enemigo.personalidad])}\"")
        
        turno = 0
        efectos = {}
        
        while jugador.vida > 0 and enemigo.vida > 0:
            turno += 1
            print(f"\n=== Turno {turno} ===")
            print(f"{jugador.nombre}: {jugador.vida}/{jugador.vida_max} HP | {enemigo.nombre}: {enemigo.vida}/{enemigo.vida_max} HP")
            
            print("\n¿Qué deseas hacer?")
            print("1. Atacar")
            print("2. Usar habilidad especial")
            print("3. Cambiar arma")
            print("4. Defender")
            print("5. Ver información del enemigo")
            
            accion_valida = False
            while not accion_valida:
                opcion = input("Selecciona una opción (1-5): ")
                
                if opcion == "1":
                    danio = jugador.ataque
                    if enemigo.defensa_activada:
                        danio = max(5, danio // 2)
                        print(f"\n¡{enemigo.nombre} se defiende y reduce el daño!")
                    enemigo.vida -= danio
                    print(f"\n¡{jugador.nombre} ataca con {jugador.arma_actual} y hace {danio} de daño a {enemigo.nombre}!")
                    accion_valida = True
                elif opcion == "2":
                    efecto = jugador.usar_especial(enemigo)
                    if efecto:
                        efectos[enemigo] = efecto
                    accion_valida = True
                elif opcion == "3":
                    if jugador.cambiar_arma():
                        accion_valida = True
                elif opcion == "4":
                    jugador.defender()
                    accion_valida = True
                elif opcion == "5":
                    enemigo.mostrar_info_detallada()
                else:
                    print("Opción no válida. Intenta de nuevo.")
            
            if enemigo.vida <= 0:
                break
            
            efectos = self.aplicar_efectos(jugador, enemigo, efectos)
            
            if enemigo.vida <= 0:
                break
            
            time.sleep(1.5)
            accion = enemigo.decidir_accion(jugador)
            
            if accion == "atacar":
                danio = enemigo.ataque
                if jugador.defensa_activada:
                    danio = max(5, danio // 2)
                    print(f"\n¡Te defiendes y reduces el daño recibido!")
                jugador.vida -= danio
                print(f"\n¡{enemigo.nombre} ataca con {enemigo.arma_actual} y te hace {danio} de daño!")
            elif accion == "especial":
                efecto = enemigo.usar_especial(jugador)
                if efecto:
                    efectos[jugador] = efecto
            elif accion == "defender":
                enemigo.defender()
            elif accion == "cambiar_arma":
                enemigo.arma_actual = random.choice(enemigo.armas)
                print(f"\n¡{enemigo.nombre} cambia a {enemigo.arma_actual}!")
            
            efectos = self.aplicar_efectos(jugador, enemigo, efectos)
            
            jugador.defensa_activada = False
            enemigo.defensa_activada = False
            
            time.sleep(1.5)
        
        if jugador.vida > 0:
            print(f"\n¡Has derrotado a {enemigo.nombre}!")
            return True
        else:
            print(f"\n¡{enemigo.nombre} te ha derrotado!")
            return False
    
    def mejorar_personaje(self, personaje):
        mejora = random.choice(["ataque", "vida", "velocidad"])
        if mejora == "ataque":
            personaje.ataque += 10
            print("\n¡Tu ataque ha aumentado en 10 puntos!")
        elif mejora == "vida":
            personaje.vida_max += 30
            personaje.vida += 30
            print("\n¡Tu vida máxima ha aumentado en 30 puntos!")
        else:
            personaje.velocidad += 15
            print("\n¡Tu velocidad ha aumentado en 15 puntos!")
    
    def mostrar_resultado(self, victorias):
        print(f"\n=== FIN DEL JUEGO ===")
        print(f"Lograste {victorias} victorias consecutivas!")
        if victorias >= 5:
            print("¡Eres un verdadero guerrero andino!")
        elif victorias >= 3:
            print("¡Buen desempeño en el campo de batalla!")
        else:
            print("¡Sigue practicando para mejorar!")
    
    def ejecutar(self):
        print("Has elegido el modo Batalla. ¡Prepárate para luchar!")
        jugador = self.elegir_personaje()
        print(f"\n¡Has elegido a {jugador.nombre}, {jugador.significado.lower()}!")
        
        victorias = 0
        while jugador.vida > 0:
            enemigo = self.crear_enemigo()
            print(f"\n¡Prepárate para la batalla {victorias + 1}!")
            
            if not self.batalla(jugador, enemigo):
                break
            
            victorias += 1
            recuperacion = min(50, jugador.vida_max - jugador.vida)
            jugador.vida += recuperacion
            jugador.especial_disponible = True
            print(f"\n¡Descansas y recuperas {recuperacion} de vida!")
            
            if victorias % 2 == 0:
                self.mejorar_personaje(jugador)
        
        self.mostrar_resultado(victorias)

class Juego:
    def __init__(self):
        self.menu_opciones = {
            "1": ("Modo Historia", self.modo_historia),
            "2": ("Modo Batalla", self.modo_batalla),
            "3": ("Salir", self.salir)
        }
    
    def modo_historia(self):
        historia = ModoHistoria()
        historia.ejecutar()
        return True
    
    def modo_batalla(self):
        batalla = ModoBatalla()
        batalla.ejecutar()
        return True
    
    def salir(self):
        print("¡Gracias por jugar! ¡Hasta la próxima!")
        return False
    
    def mostrar_menu(self):
        print("=== EL ASCENSO DEL GUERRERO ===")
        for opcion, (descripcion, _) in self.menu_opciones.items():
            print(f"{opcion}. {descripcion}")
    
    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Elige una opción (1-3): ")
            
            if opcion in self.menu_opciones:
                continuar = self.menu_opciones[opcion][1]()
                if not continuar:
                    break
            else:
                print("Opción no válida. Por favor, elige 1, 2 o 3.")

if __name__ == "__main__":
    juego = Juego()
    juego.ejecutar()
