"""
Este script elimina todos los archivos que tengan alguna extencion de las que se 
mencionan.
"""

import os
from os import remove
import shutil 
# RUTAS
path = '/home/jose/Downloads/' # Ruta donde estan las carpetas con los archivos a ordenar
# FORMATOS
extension = ("f", "java", "html", "py", "csv", "h", "pl", "c", "php", "ini", "json", "js", "cpp", "cs", "jsp", "rb", "asp", "tex", "bat", "jp2")
# Contador
num_delete = 0
num_no_delete = 0
archivos = os.listdir(path)    
for archivo in archivos: 
    ruta = f"{path}/{archivo}"
    if archivo.endswith(extension):
        remove(ruta)
        print(f"**Archivo {archivo} eliminado")
        print(f"----{num_delete} archivos eliminados")
        num_delete = num_delete + 1
    else: 
        print(f"******************************Archivo {archivo} se mantiene")
        num_no_delete = num_no_delete + 1
print(f"--------{num_delete} archivos eliminados - {num_no_delete} no eliminados--------")