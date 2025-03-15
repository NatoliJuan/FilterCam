from utils.filtros.filtro import Filtro
import cv2

class Hsv(Filtro):
    def __init__(self) -> None:
        pass

    def apply(self, img):
        solution = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        return solution
    