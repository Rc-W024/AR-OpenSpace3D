#!/usr/bin/python
# -*- coding: latin-1 -*-
#-------------------------------------------------------------------------------
# Name:        proyecta_ejes
# Purpose:
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
import numpy as np
import glob

# carga de la informacion de la calibración de la camara
# nos interesa sobre todo la matriz de camara y las distorsiones
with np.load('fotos/parametros.npz') as X:
    mtx, dist, _, _ = [X[i] for i in ('mtx','dist','rvecs','tvecs')]

# funcion para dibujar los ejes coordenados
def draw(img, corners, imgpts):
    corner = tuple(corners[0].ravel())
    cv2.line(img, corner, tuple(imgpts[0].ravel()), (255,0,0), 5)
    cv2.line(img, corner, tuple(imgpts[1].ravel()), (0,255,0), 5)
    cv2.line(img, corner, tuple(imgpts[2].ravel()), (0,0,255), 5)
    return img

# criterio de terminación (30 = numero de iteraciones; 0.001 = tolerancia sigma)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# tamano del damero sin contar las casillas de los bordes
pattern_size = (7,7)

# matriz de coordenadas de las esquinas en unidades arbitrarias (0,0,0), (1,0,0), (2,0,0) ....,(6,6,0) [sin escala]
objp = np.zeros( (np.prod(pattern_size), 3), np.float32 )
objp[:,:2] = np.indices(pattern_size).T.reshape(-1, 2)

# coordenadas en el espacio objeto de los ejes coordenados (Z negativa. hacia la camara)
axis = np.float32([[3,0,0], [0,3,0], [0,0,-3]]).reshape(-1,3)

#lista de imagenes del damero
for fname in glob.glob('fotos/*.jpg'):
    # lectura de la imagen
    img = cv2.imread(fname)
    # converion a escala de grises
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # busqueda de las esquinas del damero (coordendas imagen aproximadas)
    ret, corners = cv2.findChessboardCorners(gray, pattern_size,None)

    # si se encuentran las esquinas, se procesan
    if ret == True:
        # calculo de coordendas refinadas (en el sistema imagen)
        cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)

        # aplicacion del algoritmo Ransac para calcular las correspondencia entre los puntos en el mundo objeto y los puntos en el mundo imagen
        rvecs, tvecs, inliers = cv2.solvePnPRansac(objp, corners, mtx, dist)

        # proyecta los puntos de los ejes del sistema coordendado sobre la imagen
        imgpts, jac = cv2.projectPoints(axis, rvecs, tvecs, mtx, dist)

        # dibuja los ejes coordendados proyectados
        img = draw(img,corners,imgpts)
        # muestra la imagen con los ejes dibujados
        cv2.imshow('img',img)
        k = cv2.waitKey(0) & 0xff
        if k == 's':
            cv2.imwrite(fname[:6]+'.png', img)

cv2.destroyAllWindows()