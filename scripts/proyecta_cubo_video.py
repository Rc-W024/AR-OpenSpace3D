#!/usr/bin/python
# -*- coding: latin-1 -*-
#-------------------------------------------------------------------------------
# Name:        proyecta_cubo_video
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

with np.load('fotos/parametros.npz') as X:
    mtx, dist, _, _ = [X[i] for i in ('mtx','dist','rvecs','tvecs')]

def draw(img, corners, imgpts):
    imgpts = np.int32(imgpts).reshape(-1,2)
    cv2.drawContours(img, [imgpts[:4]],-1,(0,255,0),-3)
    for i,j in zip(range(4),range(4,8)):
        cv2.line(img, tuple(imgpts[i]), tuple(imgpts[j]),(255),3)
    cv2.drawContours(img, [imgpts[4:]],-1,(0,0,255),3)
    return img

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
pattern_size = (7,7)
objp = np.zeros( (np.prod(pattern_size), 3), np.float32 )
objp[:,:2] = np.indices(pattern_size).T.reshape(-1, 2)

cubo =np.float32([[0,0,0], [0,3,0], [3,3,0], [3,0,0],[0,0,-3],[0,3,-3],[3,3,-3],[3,0,-3] ])

# nombre de la ventana de video
cv2.namedWindow("Camera 0")
# referencia al dispositivo de captura (webcam)
captura0 = cv2.VideoCapture(0)

while (True):
    # lectura del frame actual
    res, img = captura0.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, pattern_size,None)

    if ret == True:
        cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        rvecs, tvecs, inliers = cv2.solvePnPRansac(objp, corners, mtx, dist)
        imgpts, jac = cv2.projectPoints(cubo, rvecs, tvecs, mtx, dist)
        img = draw(img,corners,imgpts)
        # dibujado del frame
        cv2.imshow('Camera 0',img)
    else:
        cv2.imshow('Camera 0',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
