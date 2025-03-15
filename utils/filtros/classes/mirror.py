import cv2
from utils.filtros.filtro import Filtro

class Mirror(Filtro):
    def __init__(self) -> None:
        pass

    def apply(self, img):
        solution = cv2.flip(img, 1)
        return solution
    
