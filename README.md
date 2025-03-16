# FilterCam

<img src="img/opencv.jpg" alt="Logo opencv" width="300">

Este proyecto es una aplicación interactiva en Python que permite procesar video en tiempo real, aplicar filtros visuales y detectar rostros. El proyecto utiliza **OpenCV** para capturar y manipular imágenes y videos en directo, y proporciona una interfaz donde los usuarios pueden activar y desactivar diferentes filtros en tiempo real mediante teclas del teclado.

## **Características**
- **Entrada de video**: Se puede usar una cámara web, un archivo de video local o un stream RTSP.
- **Filtros**: Se aplican una variedad de filtros sobre el video, tales como dilatación, erosión, filtro en escala de grises, y más. Los filtros pueden ser activados o desactivados sobre la marcha.
- **Detección de rostros**: Se realiza detección de rostros en tiempo real sobre los frames del video, utilizando un clasificador preentrenado de OpenCV.
- **Interacción**: La aplicación permite al usuario controlar el flujo de la aplicación mediante el teclado, aplicando o eliminando filtros y guardando los resultados en tiempo real.

## **Filtros disponibles**
- **Dilatación**: Expande las áreas claras de la imagen.
- **Erosión**: Reduce las áreas claras de la imagen.
- **Escala de grises**: Convierte la imagen a escala de grises.
- **HSV**: Modifica los colores de la imagen a partir del espacio de color HSV.
- **Lab**: Modifica los colores usando el espacio de color CIE-LAB.
- **Espejo**: Añade un efecto de espejo en la imagen.
- **Pixelado**: Aplica un efecto de pixelado sobre la imagen.

## **Tecnologías utilizadas**
- **Python**: Lenguaje de programación principal.
- **OpenCV**: Biblioteca para procesamiento de imágenes y video.
- **Clasificador Haar de OpenCV**: Para la detección de rostros en imágenes.

## **Instrucciones de uso**
1. Clona este repositorio en tu máquina local.
2. Instala las dependencias necesarias:
    ```bash
    pip install opencv-python
    ```
3. Configura el tipo de entrada:
    - Descomenta el input deseado:
    - Para usar un archivo de video local:
        ```python
        INPUT = Archivo("video.mp4")
        #INPUT = WebCam()
        #INPUT = Rtsp(ip="ip_videograbador",port="554", user="user", pwd ="Password")
        ```
    - Para usar una cámara web:
        ```python
        #INPUT = Archivo("video.mp4")
        INPUT = WebCam()
        #INPUT = Rtsp(ip="ip_videograbador",port="554", user="user", pwd ="Password")
        ```
    - Para usar un stream RTSP:
        ```python
        #INPUT = Archivo("video.mp4")
        #INPUT = WebCam()
        INPUT = Rtsp(ip="ip_videograbador",port="554", user="user", pwd ="Password")
        ```
5. Ejecuta el script:
    ```bash
    python main.py
    ```
6. Cambia de filtros:
Con los números del 1 al 6 se puede activar y desactivar los filtros.

## **Autor**
Juan Natoli
