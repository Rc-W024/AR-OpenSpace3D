#-------------------------------------------------------------------------------
# Name:        extrae_frames
# Purpose:
#
# Author:      jpalomav
# Modif:       RC-W
#
# Created:     20/11/2015
# Modif:       27/01/2023
# Copyright:   (c) jpalomav 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import cv2

try:

    # acceso al video (testeado con avi y mp4)
    captura = cv2.VideoCapture('C:\\opencv_python\\scripts\\lago_silencia.avi')

    contador = 0
    while True:
        # captura frame a frame
        success, frame = captura.read()
        if success == False:
            break
        # se escribe cada frame con su numero de orden
        if contador % 10 == 0: # en este caso se extrae un frame de cada 10
            cv2.imwrite("lago_silencia\\frame%d.tif" % contador, frame)
        contador += 1
    # liberar el dispositivo y cerrar ventanas
    captura.release()

except:
    captura.release()