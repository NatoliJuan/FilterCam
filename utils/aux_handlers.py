import cv2
from main import FILTROS
from screeninfo import get_monitors


def apply_filters(imagen,filtros_aplicados):
    aux_img = imagen
    valor2 = 50
    for posicion, valor in filtros_aplicados.items():
        if valor == True:
            filtro = FILTROS[posicion]
            aux_img = filtro.apply(aux_img)
            valor2 += 50
    return aux_img

def exit_key(tecla_pulsada):
    if tecla_pulsada == 27: 
        cv2.destroyAllWindows()
        exit()

def añadir_eliminar_filtros(tecla_pulsada, filtros_aplicados):
    aux_teclado = tecla_pulsada - 48
    if aux_teclado in filtros_aplicados:
        filtros_aplicados[aux_teclado] = not filtros_aplicados[aux_teclado] 


def contruir_filtros_aplicados(): 
    filtros = {}
    for filtro in range(len(FILTROS)):
        filtros[filtro] = False             
    return filtros
    
def pantalla_completa():
    cv2.namedWindow('Imagen en pantalla completa', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Imagen en pantalla completa', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

def ajustar_resolucion(imagen):
    monitor = get_monitors()[0]
    pantalla_ancho = monitor.width
    pantalla_alto = monitor.height
    imagen_final = cv2.resize(imagen, (pantalla_ancho, pantalla_alto),interpolation=cv2.INTER_NEAREST)
    return imagen_final


def mostrar_filtros_en_imagen(imagen, filtros, filtros_aplicados):

    numero_caracteres_filtro_mas_largo = 0
    for filtro in filtros:
        nombre_filtro = type(filtro).__name__
        longitud = len(nombre_filtro)
        if longitud > numero_caracteres_filtro_mas_largo:
            numero_caracteres_filtro_mas_largo = longitud
                     

    sol_string = []
    for posicion, es_encendido in filtros_aplicados.items():
        objeto_filtro = filtros[posicion] 
        nombre_filtro = type(objeto_filtro).__name__

        espacios = " " * (numero_caracteres_filtro_mas_largo - len(nombre_filtro))
        sol_string.append(f"{posicion}. {nombre_filtro}: {espacios}{es_encendido}")
    
    aux_img = imagen
    
    aux_img = cv2.rectangle(aux_img, (25, 0), (800, 50 * (len(sol_string) +1)), (255, 255, 255), -1)
    i=1
    for cadena in sol_string:
        aux_img = cv2.putText(aux_img,cadena,(25, 50*i),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,0),2)
        i+=1
    
    return aux_img

def guardar_videos(imagen, frames):

# Obtener la tasa de frames por segundo (fps) y la resolución del video
    fps = imagen(cv2.CAP_PROP_FPS)
    ancho = int(imagen(cv2.CAP_PROP_FRAME_WIDTH))
    alto = int(imagen(cv2.CAP_PROP_FRAME_HEIGHT))

    video_salida = 'video_salida.mp4'

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(video_salida, fourcc, fps, (ancho, alto))

    for frame in frames:
        video_writer.write(frame)

def detectar_rostro(imagen):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Convertir a escala de grises
    gray_image = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Detectar rostros
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    # Dibujar rectángulos alrededor de los rostros detectados
    for (x, y, w, h) in faces:
        cv2.rectangle(imagen, (x, y), (x + w, y + h), (255, 0, 0), 2)
