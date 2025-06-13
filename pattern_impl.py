from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    @abstractmethod
    def update(self, message: str) -> None:
        pass

class Subject(ABC):
    @abstractmethod
    def add_observer(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify_observers(self, message: str) -> None:
        pass

class NewsAgency(Subject):
    def __init__(self):
        self._observers: List[Observer] = []
        self._news: str = ""

    def add_observer(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify_observers(self, message: str) -> None:
        if not message:
            raise ValueError("News message cannot be empty")
        self._news = message
        for observer in self._observers:
            observer.update(message)

    def add_news(self, news: str) -> None:
        self.notify_observers(news)

class EmailSubscriber(Observer):
    def __init__(self, email: str):
        if not email or "@" not in email:
            raise ValueError("Invalid email address")
        self.email = email

    def update(self, message: str) -> None:
        print(f"Email sent to {self.email}: {message}")

class SMSSubscriber(Observer):
    def __init__(self, phone: str):
        if not phone or not phone.startswith("+"):
            raise ValueError("Invalid phone number")
        self.phone = phone

    def update(self, message: str) -> None:
        print(f"SMS sent to {self.phone}: {message}")