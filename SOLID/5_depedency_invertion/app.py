# Depender sempre da interface, nunca da implementação. Referenciar sempre abstrações, e não concreções

from .notificator_interface import NotificatorInterface

class ClientService:
    def __init__(self, notificator: NotificatorInterface) -> None:
        self.notificator = notificator

    def send(self, message: str) -> None:
        self.notificator.send_notification(message)