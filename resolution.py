"""
This script is for delete images if the resolution is minor that 600px
"""

import os
from PIL import Image, UnidentifiedImageError
from os import remove
import shutil 
# ROUTES
path = '/home/jose/Downloads/backup/img' # Route of the images
# COUNTER
num = 0
archivos = os.listdir(path)    
for archivo in archivos: 
    try:
        ruta_archivo = f"{path}/{archivo}"
        img_size = Image.open(ruta_archivo)
        width, height = img_size.size
        
        if(height <= 600 or width <= 600):
            print(f"---Archivo {archivo} se elimina: ({width},{height})")
            remove(ruta_archivo)
            num = num + 1
        else:
            print(f"Archivo {archivo} se mantiene")
        print(f"-----------------Se eliminaron {num} archivos")
    except UnidentifiedImageError:
        print(f"cannot identify image file {archivo}")        
print(f"-------------**Se eliminaron {num} archivos**------------------------")
    
               
        