from utils.filtros.filtro import Filtro
import cv2

class Gris(Filtro):
    def __init__(self) -> None:
        pass

    def apply(self, img):
        solution = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return solution
    