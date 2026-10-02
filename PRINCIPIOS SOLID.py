class Reporte:
    def __init__(self, contenido):
        self.contenido = contenido


class GuardadorReporte:
    def guardar(self, reporte: Reporte, ruta: str):
        with open(ruta, "w") as f:
            f.write(reporte.contenido)

class Descuento:
    def aplicar(self, precio):
        return precio


class DescuentoVIP(Descuento):
    def aplicar(self, precio):
        return precio * 0.8


class DescuentoEstudiante(Descuento):
    def aplicar(self, precio):
        return precio * 0.9

class Ave:
    pass
class AveVoladora(Ave):
        def volar(self):
            return "Volando..."
class Pinguino(Ave):
    def nadar(self):
        return "Nadando..."