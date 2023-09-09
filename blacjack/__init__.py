class Carta:

    def __init__(self, pinta: str, valor: str):
        self.pinta: str = pinta
        self.valor: str = valor
        self.tapada: bool = False



class Baraja:

    def __init__(self):
        self.cartas: list[Carta] = []


    def revolver(self):
        pass


    def repartir_carta(self, tapada: bool)->Carta:
        pass


class Casa:

    def __init__(self):
        pass

    def inicializar_mano(self):
        pass


    def destapar_cas(self):
        pass


    def calcular_manocasa(self):
        pass

class Mano:

    def __init__(self, cartas):
        self.cartas = cartas


    def es_blackjack(self)->bool:
        pass


    def comparar_mano(self):
        pass


    def valor(self):
        pass


class blackjack:
    def __init__(self):
        pass

    def registrar_jugador(self, nombre: str):
        self.nombre: str = nombre

    def iniciar_juego(self, apuesta: int):
        self.apuesta: int = apuesta

    def jugada_jugador(self):
        pass

    def doblar_fichas(self):
        pass

    def menu(self):
        pass

    def restar_fichas(self):
        pass

    def devolver_fichas(self):
        pass

    def fichas_disponibles(self):
        pass

    def mostrar_ganador(self):
        pass

class Jugador:

    def __init__(self, nombre : str, fichas : int):
        self.nombre: str = nombre
        self.fichas: int = fichas


    def inicializar_mano(self, cartas):
        self.cartas = cartas

    def pedir_cartas(self):
        pass

    def jugador_planta(self):
        pass

    def exit(self):
        pass




