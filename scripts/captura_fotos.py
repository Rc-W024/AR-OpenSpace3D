#!/usr/bin/python
# -*- coding: latin-1 -*-
#-------------------------------------------------------------------------------
# Name:        captura_foto
# Purpose:     captura fotos a partir de una webCam
#
# Author:      jpalomav
# Modif:       RC-W
#
# Created:     20/11/2015
# Modif:       27/01/2023
# Copyright:   (c) jpalomav 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import cv2

# nombre de la ventana de la webcam
cv2.namedWindow("WebCam")
n = 0
try:
    # dispositivo de captura (si se tiene mas de una webcam el id cambia)
    captura = cv2.VideoCapture(0)
    while (True):
            # captura frame a frame (devuelve el frame y un valor ret que es true o false)
            ret, frame = captura.read()
            if ret:
                # se muestra el frame
                cv2.imshow('WebCam',frame)
                # espera a que pulsemos una tecla 25 milisegundos. Esto da tiempo tambien al refresco del frame
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    #si la tecla es "q" sale del bucle para cerrar la ventana
                    break
                 # si la tecla es "s" salva el frame como un archivo jpg
                if cv2.waitKey(25) & 0xFF == ord('s'):
                    cv2.imwrite('fotos/foto'+str(n)+'.jpg',frame)
                    n += 1

    # liberar el dispositivo y cerrar ventanas
    captura.release()
    cv2.destroyAllWindows()

except:
    captura.release()
    cv2.destroyAllWindows()