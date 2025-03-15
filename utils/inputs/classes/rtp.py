from utils.inputs.input import Input
import cv2

class Rtsp(Input):
    def __init__(self, ip, port,user,pwd):
        super().__init__()

        aux = f"rtsp://{user}:{pwd}@{ip}:{port}/(h264/MPEG-4)/ch01/(main/sub)/av_stream"

        self.cam = cv2.VideoCapture(aux)
        if(self.cam.isOpened()):
            self.opened = True
        else:
            print("Imposible de conectar")
            exit()
    
    def get_image(self):
        ret_val, img = self.cam.read()
        return img
    