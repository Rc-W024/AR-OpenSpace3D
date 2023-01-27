#!/usr/bin/python
# -*- coding: latin-1 -*-
#-------------------------------------------------------------------------------
# Name:        detecta_puntos
# Purpose:     detecta las esquinas a partir de las fotos de un damero
#
# Author:      jpalomav
# Modif:       RC-W
#
# Created:     20/11/2015
# Modif:       27/01/2023
# Copyright:   (c) jpalomav 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# libreria para tratamiento de matrices
import numpy as np
# libreria de visión por computador
import cv2
# libreria para la búsqueda de ficheros con patrones de cadena
import glob

# criterio de terminacion del algoritmo (30 = numero de iteraciones; 0.001 = tolerancia sigma)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# numero de esquinas a detectar sin contar las casillas de los bordes
pattern_size = (7,7) #nuestro damero es de 8x8

# matriz de coordenadas de las esquinas en unidades arbitrarias (0,0,0), (1,0,0), (2,0,0) ....,(6,6,0) [sin escala]
objp = np.zeros( (np.prod(pattern_size), 3), np.float32 ) #matriz de
objp[:,:2] = np.indices(pattern_size).T.reshape(-1, 2)

# arrays para almacenar los puntos objeto y los puntos imagen de todas las imagenes.
objpoints = [] # puntos 3d en el espacio real (el sistema de coordendas es el definido por nosotros).
imgpoints = [] # puntos 2d en el plano de la imagen.

# lista de imagenes del damero
images = glob.glob('fotos/*.jpg')

for fname in images:
    # carga de la imagen
    img = cv2.imread(fname)
    # conversion de la imagen en color a escala de grises
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # busqueda de las esquinas del damero (coordendas imagen aproximadas)
    ret, corners = cv2.findChessboardCorners(gray, pattern_size,None)

    # si se encuentran las esquinas, se anaden los puntos objeto y los puntos imagen tras refinarlos
    if ret == True:
        objpoints.append(objp)
        # refinado de las esquinas a nivel subpixel (1/2 tamano de ventana de busqueda)
        cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners)

        # dibuja las esquinas sobre la imagen
        cv2.drawChessboardCorners(img, pattern_size, corners,ret)
        # visualiza la imagen en una ventana
        cv2.imshow('img',img)
        # espera 1 segundo a que pulsemos una tecla y continua
        cv2.waitKey(1000)

cv2.destroyAllWindows()