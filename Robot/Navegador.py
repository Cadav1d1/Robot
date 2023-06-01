class Navegador:
    def __init__(self):
        self.camino = []

    def definir_camino(self, camino):
        self.camino = camino

    def seguir_camino(self):
        if len(self.camino) > 0:
            siguiente_punto = self.camino.pop(0)
            return f"Siguiendo el camino hacia {siguiente_punto}"
        else:
            return "Se ha llegado al destino final"

    def agregar_punto(self, punto):
        self.camino.append(punto)
        return f"Punto {punto} agregado al camino"
