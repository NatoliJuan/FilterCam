from abc import ABC, abstractmethod

class Input(ABC):
    def __init__(self):
        pass
    

    @abstractmethod
    def get_image(self):
        pass
