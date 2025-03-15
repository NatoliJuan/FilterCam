from utils.inputs.input import Input
import cv2

class Archivo(Input):
    def __init__(self, ruta_archivo):
        super().__init__()

        self.cam = cv2.VideoCapture(ruta_archivo)
    
    def get_image(self):
        ret_val, img = self.cam.read()
        return img
    