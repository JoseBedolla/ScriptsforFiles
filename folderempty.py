"""
Este script elimina las carpetas vacias dentro de una carpeta.
"""

import os
from os import rmdir
import shutil 
# RUTAS
path = '/home/jose/Documents' # Ruta donde estan las carpetas 

carpetas = os.listdir(path)    
for carpeta in carpetas: 
    ruta = f"{path}/{carpeta}"
    if os.listdir(ruta) == []:
        print(f"La carpeta {carpeta} no contiene archivos, ELIMINADA")
        rmdir(ruta)
    else: 
        print(f"La carpeta {carpeta} contiene archivos...")
        