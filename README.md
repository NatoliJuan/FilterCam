# FilterCam

<img src="img/opencv.jpg" alt="Logo opencv" width="300">

Este proyecto es una aplicación interactiva en Python que permite procesar video en tiempo real, aplicar filtros visuales y detectar rostros. El proyecto utiliza **OpenCV** para capturar y manipular imágenes y videos en directo, y proporciona una interfaz donde los usuarios pueden activar y desactivar diferentes filtros en tiempo real mediante teclas del teclado.

## **Características**

### 🎥 **Entrada de video**
Se puede usar una cámara web, un archivo de video local o un stream RTSP.

### 🔲 **Filtros**
Se aplican una variedad de filtros sobre el video, tales como dilatación, erosión, filtro en escala de grises, y más. Los filtros pueden ser activados o desactivados sobre la marcha.

### 👤 **Detección de rostros**
Se realiza detección de rostros en tiempo real sobre los frames del video, utilizando un clasificador preentrenado de OpenCV.

### ⌨️ **Interacción**
La aplicación permite al usuario controlar el flujo de la aplicación mediante el teclado, aplicando o eliminando filtros y guardando los resultados en tiempo real.

## **Filtros disponibles**

- 🔳 **Dilatación**: Expande las áreas claras de la imagen.
- ⚪ **Erosión**: Reduce las áreas claras de la imagen.
- ⚫ **Escala de grises**: Convierte la imagen a escala de grises.
- 🌈 **HSV**: Modifica los colores de la imagen a partir del espacio de color HSV.
- 🎨 **Lab**: Modifica los colores usando el espacio de color CIE-LAB.
- 🔄 **Espejo**: Añade un efecto de espejo en la imagen.
- 🟢 **Pixelado**: Aplica un efecto de pixelado sobre la imagen.

## **Tecnologías utilizadas**

- 🐍 **Python**: Lenguaje de programación principal.
- 🖼️ **OpenCV**: Biblioteca para procesamiento de imágenes y video.
- 🤖 **Clasificador Haar de OpenCV**: Para la detección de rostros en imágenes.

## **Instrucciones de uso**

1. **Instala las dependencias necesarias**:
    ```bash
    pip install opencv-python
    ```

2. **Configura el tipo de entrada**:
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

3. **Ejecuta el script**:
    ```bash
    python main.py
    ```

4. **Cambia de filtros**:  
   Con los números del 1 al 6 puedes activar y desactivar los filtros.  

## **Descripción del código**

### 📝 **Cómo hice el código**

- **Estructura del código**: El proyecto está estructurado de manera modular, utilizando clases y funciones para manejar cada filtro y entrada de video por separado. Esto permite un fácil mantenimiento y ampliación del proyecto en el futuro.
  
- **Entradas de video**: Se permite la opción de elegir entre diferentes tipos de entradas de video (cámara web, archivo o stream RTSP) mediante clases específicas (`WebCam`, `Archivo`, `Rtsp`), las cuales se definen en archivos separados bajo el directorio `utils/inputs/classes/`.

- **Filtros**: Los filtros como dilatación, erosión, escala de grises, HSV, y otros se implementan en clases, cada una dentro del directorio `utils/filtros/classes/`. Cada filtro tiene su propio método `apply` que se llama sobre los frames del video.

- **Detección de rostros**: Se emplea el clasificador Haar de OpenCV para detectar rostros en los frames del video. Este proceso se realiza sobre la marcha, asegurando que la detección se realice en tiempo real.

- **Interactividad**: La aplicación está diseñada para que el usuario pueda interactuar con ella fácilmente utilizando el teclado. Los filtros se activan y desactivan con las teclas del 1 al 6. Los cambios en la configuración de los filtros se manejan mediante la función `añadir_eliminar_filtros`.

- **Guardado de resultados**: Los frames procesados se almacenan en una lista y luego se guardan en un video al final de la ejecución del programa. Esto permite al usuario guardar el resultado de la aplicación de filtros en tiempo real.

## **Autor**
Juan Natoli
