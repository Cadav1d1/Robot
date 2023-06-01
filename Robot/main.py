from Robot import Robot
from Navegador import Navegador
from RobotUI import RobotUI

from tkinter import messagebox

if __name__ == "__main__":
    robot = Robot()
    navegador = Navegador()

    # Definir el camino
    camino = ["Punto A", "Punto B", "Punto C", "Punto D"]
    navegador.definir_camino(camino)

    app = RobotUI(robot, navegador)
    app.mainloop()
