class Robot:
    def __init__(self):
        self.estado_actual = "Robot Apagado"
        self.basura_reciclable = 0
        self.basura_no_reciclable = 0

    def encender(self):
        if self.estado_actual == "Robot Apagado":
            self.estado_actual = "Robot Encendido"
            return "El robot se ha encendido"
        else:
            return "El robot ya está encendido"

    def apagar(self):
        if self.estado_actual == "Robot Encendido":
            self.estado_actual = "Robot Apagado"
            return "El robot se ha apagado"
        else:
            return "El robot ya está apagado"

    def recolectar_objeto(self):
        if self.estado_actual == "Robot Encendido":
            self.basura_reciclable += 1
            return "Objeto recolectado correctamente"
        else:
            return "El robot debe estar encendido para recolectar objetos"

    def botar_reciclable(self):
        if self.estado_actual == "Robot Encendido":
            if self.basura_reciclable > 0:
                self.basura_reciclable -= 1
                return "Basura reciclable botada correctamente"
            else:
                return "No hay basura reciclable para botar"
        else:
            return "El robot debe estar encendido para botar basura"

    def botar_no_reciclable(self):
        if self.estado_actual == "Robot Encendido":
            if self.basura_no_reciclable > 0:
                self.basura_no_reciclable -= 1
                return "Basura no reciclable botada correctamente"
            else:
                return "No hay basura no reciclable para botar"
        else:
            return "El robot debe estar encendido para botar basura"

    def soltar_objetos(self):
        if self.estado_actual == "Robot Encendido":
            if self.basura_reciclable > 0 or self.basura_no_reciclable > 0:
                total_objetos = self.basura_reciclable + self.basura_no_reciclable
                self.basura_reciclable = 0
                self.basura_no_reciclable = 0
                return "Objetos soltados correctamente. Total objetos soltados: {}".format(total_objetos)
            else:
                return "No hay objetos para soltar"
        else:
            return "El robot debe estar encendido para soltar objetos"

    def parado_de_emergencia(self):
        if self.estado_actual == "Robot Encendido":
            self.estado_actual = "Parado de Emergencia"
            return "Parado de emergencia. Robot apagado"
        else:
            return "El robot ya está apagado"

    def continuar(self):
        if self.estado_actual == "Parado de Emergencia":
            self.estado_actual = "Robot Encendido"
            return "Continuando operaciones"
        else:
            return "El robot ya está encendido"