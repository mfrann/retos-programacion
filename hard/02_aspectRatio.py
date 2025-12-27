'''
#TODO:
/*
 * Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url de ejemplo:
 *   https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 *   imagen de 1920*1080px.
*/
'''
#===LIBRERIAS===#

import requests as rq
from PIL import Image
from io import BytesIO
import math

def aspect_ratio(url):

    try:
        response = rq.get(url, timeout=10) #Obtenemos la URL
        response.raise_for_status() #Vemos el status

        imagen = Image.open(BytesIO(response.content)) #Guardamos en imagen

        ancho, alto = imagen.size #Calculamos y guardamos el ancho y alto de la imagen

        mcd = math.gcd(ancho, alto) #Calculamos su MCD

        ratio_ancho = ancho // mcd # Division entera redondeada a abajo
        ratio_alto = alto // mcd

        return {
            'ancho': ancho,
            'alto': alto,
            'ratio': f'{ratio_ancho}:{ratio_alto}'
        }
    
    except Exception as e: #Comprobar error
        print(f'Error: {e}')


print(aspect_ratio('https://th.bing.com/th/id/R.f4ad1bfc4a9ca9828e4874e2398ecb7e?rik=ApXjBJYzWpbskg&pid=ImgRaw&r=0'))
