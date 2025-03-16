from utils.aux_handlers import *
from utils.filtros.classes.dilatacion import Dilatacion
from utils.filtros.classes.erosion import Erosion
from utils.filtros.classes.gris import Gris
from utils.filtros.classes.hsv import Hsv
from utils.filtros.classes.lab import Lab
from utils.filtros.classes.mirror import Mirror
from utils.filtros.classes.pixelado import Pixelado
from utils.inputs.classes.archivo import Archivo
from utils.inputs.classes.rtp import Rtsp
from utils.inputs.classes.webcam import WebCam
import cv2


#INPUT = Archivo("video.mp4")
INPUT = WebCam()
#INPUT = Rtsp(ip="ip_videograbador",port="554", user="user", pwd ="Password")
FILTROS = [Lab(), Erosion(), Dilatacion(), Mirror(), Hsv(), Gris(), Pixelado()]

# Cargar el clasificador de rostros

def main():
    filtros_aplicados = contruir_filtros_aplicados()
    frames = []

    while True:
        #0. Comprobamos tecla pulsada
        tecla_pulsada = cv2.waitKey(1)

        #1. Comprobamos si tenemos que aplicar o desaplicar un filtro segun la tecla que se ha pulsado
        añadir_eliminar_filtros(tecla_pulsada, filtros_aplicados)

        #2.  Obtenemos imagen de entrada
        img = INPUT.get_image() 

        #3 Detectar rostros
        detectar_rostro(img)

        #4. Aplicamos filtros
        img = apply_filters(img,filtros_aplicados)

        #5. Guardamos frame en lista
        frames.append(img)

        #6. Pantalla completa
        pantalla_completa()
        img = ajustar_resolucion(img)

        #7. Imprimimos nombres de los filtros a la imagen y si estan activados o no
        img = mostrar_filtros_en_imagen(img, filtros=FILTROS, filtros_aplicados=filtros_aplicados)
        
        #8. Mostramos Imagen
        img = cv2.imshow('Proyecto Camera', img)

        #9 Guardamos el video
        guardar_videos(INPUT.cam.get, frames)

        #10. Comprobamos si queremos salir   
        exit_key(tecla_pulsada)
       

if __name__ == '__main__':
    main()
