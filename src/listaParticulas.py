from Particula import Particula


class listaParticula:
    def __init__(self):
        self.__particulas = []

    def agregar_inicio(self, particula: Particula):
        self.__particulas.insert(0, particula)

    def agregar_final(self, particula: Particula):
        self.__particulas.append(particula)

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)


""" id, origen_x, origen_y, destino_x, destino_y, veloicidad, red, green, blue, distancia """
particula1 = Particula(1, 5, 5, 10, 15, 3, 100, 100, 100, 0)
particula2 = Particula(2, 0, 10, 2, 12, 2, 200, 200, 200, 0)
particula3 = Particula(3, 7, 5, 4, 20, 6, 255, 100, 100, 0)

lista = listaParticula()

lista.agregar_inicio(particula3)
lista.agregar_inicio(particula2)
lista.agregar_inicio(particula1)

lista.mostrar()
