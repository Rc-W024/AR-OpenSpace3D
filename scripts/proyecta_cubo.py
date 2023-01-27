#!/usr/bin/python
# -*- coding: latin-1 -*-
#-------------------------------------------------------------------------------
# Name:        proyecta_cubo
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

with np.load('fotos/parametros.npz') as X:
    mtx, dist, _, _ = [X[i] for i in ('mtx','dist','rvecs','tvecs')]

# funcion para dibujar el cubo
def draw(img, corners, imgpts):
    imgpts = np.int32(imgpts).reshape(-1,2)
    # dibuja la base en color verde y la rellena
    cv2.drawContours(img, [imgpts[:4]],-1,(0,255,0),-3)
    # dibuja los lilares en color azul
    for i,j in zip(range(4),range(4,8)):
        cv2.line(img, tuple(imgpts[i]), tuple(imgpts[j]),(255),3)
    # dibuja la tapa en color rojo
    cv2.drawContours(img, [imgpts[4:]],-1,(0,0,255),3)

    return img

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
pattern_size = (7,7)
objp = np.zeros( (np.prod(pattern_size), 3), np.float32 )
objp[:,:2] = np.indices(pattern_size).T.reshape(-1, 2)

# coordenadas 3d de las 8 esquinas del cubo en el sistema de referencia del damero
cubo =np.float32([[0,0,0], [0,3,0], [3,3,0], [3,0,0],[0,0,-3],[0,3,-3],[3,3,-3],[3,0,-3] ])

for fname in glob.glob('fotos/*.jpg'):
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, pattern_size,None)
    if ret == True:
        cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        rvecs, tvecs, inliers = cv2.solvePnPRansac(objp, corners, mtx, dist)
        imgpts, jac = cv2.projectPoints(cubo, rvecs, tvecs, mtx, dist)

        img = draw(img,corners,imgpts)
        cv2.imshow('img',img)
        k = cv2.waitKey(0) & 0xff
        if k == 's':
            cv2.imwrite(fname[:6]+'.png', img)

cv2.destroyAllWindows()
