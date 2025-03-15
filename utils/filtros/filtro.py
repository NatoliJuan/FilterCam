from abc import ABC, abstractmethod

class Filtro(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def apply(self, img):
        pass
        