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


from abc import ABC, abstractmethod


class Impresora(ABC):
    @abstractmethod
    def imprimir(self):
        pass


class Escaner(ABC):
    @abstractmethod
    def escanear(self):
        pass


class ImpresoraSencilla(Impresora):
    def imprimir(self):
        print("Imprimiendo documento...")

        from abc import ABC, abstractmethod

        class ServicioMensaje(ABC):
            @abstractmethod
            def enviar(self, msg):
                pass

        class ServicioSMS(ServicioMensaje):
            def enviar(self, msg):
                print(f"SMS: {msg}")

        class ServicioEmail(ServicioMensaje):
            def enviar(self, msg):
                print(f"Email: {msg}")

        class Notificador:
            def __init__(self, servicio: ServicioMensaje):
                self.servicio = servicio

            def enviar_alerta(self, msg):
                self.servicio.enviar(msg)

