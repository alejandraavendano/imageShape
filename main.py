'''Pontificia Universidad Javeriana
   Procesamiento de imagenes y visión
   Alejandra Isabel Avendaño Cortina'''


from imageShape import *

if __name__ == '__main__':

    width = input('Insertar el ancho de la imagen ') #Se pide insertar el valor de ancho
    height = input('Insertar el alto de la imagen ') #Se pide insertar el valor de alto
    shape = imageShape(int(width), int(height))
    shape.generateShape()

