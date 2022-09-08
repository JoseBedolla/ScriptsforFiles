"""
Este script es para ordenar una gran cantidad de archivos y asignarlos a una carpeta
segun su extension. 
"""

import os
from pydoc import doc 
import shutil 
# RUTAS
path = '/home/jose/Pictures' # Ruta donde estan las carpetas con los archivos a ordenar
imagenes = '/home/jose/Downloads/code/img' # Ruta donde se guardaran las imagenes
videos = '/home/jose/Downloads/code/videos' # Ruta donde se guardaran los videos
textos = '/home/jose/Downloads/code/texto' # Ruta donde se guardaran los archivos de texto
documentos = '/home/jose/Downloads/code/office' # Ruta donde se guardaran los archivos de office
otros = '/home/jose/Downloads/code/otros' # Si no es de ninguna extension se asignara aqui
# EXTENSIONES
img = ('png', 'jpg', 'jpeg', 'psd', 'gif', 'tif')
texto =('txt')
office = ('docx', 'xlsx', 'pptx')
video = ('mp4', 'mov', 'wmv', 'avi', 'webm')
# CONTADORES
num_textos = 0
num_img = 0
num_videos = 0
num_office = 0
num_otros = 0

carpetas = os.listdir(path)    
for carpeta in carpetas: 
    ruta = f"{path}/{carpeta}"
    print(f"Entrando a la carpeta {ruta}...") 
    archivos = os.listdir(ruta)
    for archivo in archivos:
        if archivo.endswith(img):
            print(f"--Archivo {archivo} asignado a {imagenes}") 
            shutil.move(f"{ruta}/{archivo}", f"{imagenes}/{num_img}_{archivo}")
            num_img =+ 1
            continue
        if archivo.endswith(texto):
            print(f"--Archivo {archivo} asignado a {textos}")            
            shutil.move(f"{ruta}/{archivo}", f"{textos}/{num_textos}_{archivo}")
            num_textos =+ 1
            continue
        if archivo.endswith(office):
            print(f"--Archivo {archivo} asignado a {documentos}") 
            shutil.move(f"{ruta}/{archivo}", f"{documentos}/{num_office}_{archivo}")
            num_office =+ 1
            continue
        if archivo.endswith(video):
            print(f"--Archivo {archivo} asignado a {videos}") 
            shutil.move(f"{ruta}/{archivo}", f"{videos}/{num_videos}_{archivo}")
            num_videos =+ 1
            continue
       
        else: 
            print(f"--Archivo {archivo} asignado a {otros}") 
            shutil.move(f"{ruta}/{archivo}", f"{otros}/{num_otros}_{archivo}")
            num_otros =+ 1
            continue
               