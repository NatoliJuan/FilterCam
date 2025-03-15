from utils.inputs.input import Input
import cv2

class WebCam(Input):
    def __init__(self):
        super().__init__()

        self.cam = cv2.VideoCapture(0)
    
    def get_image(self):
        ret_val, img = self.cam.read()
        return img
    

        
