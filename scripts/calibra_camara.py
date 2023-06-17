#!/usr/bin/python
# -*- coding: latin-1 -*-
#-------------------------------------------------------------------------------
# Name:        calibra_camara
# Purpose:     calibra una camara a partir de los datos de un damero
#
# Author:      jpalomav
# Modif:       RC-W
#
# Created:     20/11/2015
# Modif:       27/01/2023
# Copyright:   (c) jpalomav 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np
import cv2
import glob

# criterio de terminacion (30 = numero de iteraciones; 0.001 = tolerancia sigma)
criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# tamano del damero sin contar las casillas de los bordes
pattern_size=(7,7)

# matriz de coordenadas de las esquinas en unidades arbitrarias (0,0,0), (1,0,0), (2,0,0) ....,(6,6,0) [sin escala]
objp=np.zeros( (np.prod(pattern_size), 3), np.float32 )
objp[:,:2]=np.indices(pattern_size).T.reshape(-1, 2)

# arrays para almacenar los puntos objeto y los puntos imagen de todas las imagenes.
objpoints=[] # puntos 3d en el espacio real (el sistema de coordendas es el definido por nosotros).
imgpoints=[] # puntos 2d en el plano de la imagen.

# lista de imagenes del damero
images=glob.glob('fotos/*.jpg')

for fname in images:
    img=cv2.imread(fname)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # busqueda de las esquinas del damero (coordendas imagen aproximadas)
    ret, corners=cv2.findChessboardCorners(gray, pattern_size,None)

    # si se encuentran las esquinas, se anaden los puntos objeto y los puntos imagen tras refinarlos
    if ret==True:
        objpoints.append(objp)
        # refinado de las esquinas a nivel subpixel (1/2 tamano de ventana de busqueda)
        cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners)

        # dibuja las esquinas sobre la imagen
        cv2.drawChessboardCorners(img, pattern_size, corners,ret)
        cv2.imshow('img',img)
        cv2.waitKey(1000)

cv2.destroyAllWindows()

# obtiene los parametros de calibracion a partir de las coordenadas objeto e imagen de todas las fotos
# ret: True o False
# mtx: matriz de la camara o intrinseca [[fx,0,cx],[0,fy,cy],[0,0,1]] -> focal y coordenadas del punto principal
# dist: distorsiones k1, k2, k3, p1, p2
# rvecs: matriz de rotacion (extrinseca)
# matriz de traslacion (extrinseca)
ret, mtx, dist, rvecs, tvecs=cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
print mtx
print 100*'-'
print dist
print 100*'-'
print rvecs
print 100*'-'
print tvecs
print 100*'-'

# salvamos los parametros en un fichero binario para el siguiente script
np.savez('fotos/parametros.npz',mtx=mtx,dist=dist,rvecs=rvecs,tvecs=tvecs)

