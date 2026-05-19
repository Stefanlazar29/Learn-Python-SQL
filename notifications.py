
from abc import ABC, abstractmethod

# 1. Clasa Abstractă (Contractul)
class Notification(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass

# 2. Clase Concrete
class EmailNotifications(Notification):
    def send(self, message: str) -> None:
        print(f"Trimitere Email: {message}")

class SMSNotifications(Notification):
    def send(self, message: str) -> None:
        print(f"Send SMS: {message}")

# 3. Funcție de procesare (Polimorfism)
def process_notifications(notifications: list[Notification], message: str) -> None:
    for n in notifications:
        n.send(message)

# 4. Execuție
if __name__ == "__main__":
    notifs = [EmailNotifications(), SMSNotifications()]
    process_notifications(notifs, "The system is alive!")

