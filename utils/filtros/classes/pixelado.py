import cv2
from utils.filtros.filtro import Filtro

class Pixelado(Filtro):
    def __init__(self) -> None:
        pass

    def apply(self, img):
        w, h = (32, 32)
        return cv2.resize(img, (w, h), interpolation=cv2.INTER_LINEAR)