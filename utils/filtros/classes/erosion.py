from utils.filtros.filtro import Filtro
import cv2

class Erosion(Filtro):
    def __init__(self) -> None:
        pass

    def apply(self, img):
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        solution = cv2.erode(img, kernel, iterations=1)
        return solution
    



