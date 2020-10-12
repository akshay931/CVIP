import cv2 as cv
import math as m
import numpy as np
img = cv.imread('plane.tiff')
row,col,channel = img.shape
cv.imshow("image",img)
#img = img.astype(np.uint)
filt = [-1,-2,-1,-2,12,-2,-1,-2,-1]
image1 = img
# 3x3 default filter applied
for x in range(0,row-1):
    for y in range(0,col-1):
        temp1 = ((img[x,y][0]*filt[4])+(img[x-1,y-1][0]*(filt[0]))+(img[x-1,y][0]*(filt[1]))+(img[x-1,y+1][0]*(filt[2]))+(img[x,y-1][0]*(filt[3]))+(img[x,y+1][0]*(filt[5]))+(img[x+1,y-1][0]*(filt[6]))+(img[x+1,y][0]*(filt[7]))+(img[x+1,y+1][0]*(filt[8])))/16

        temp2 = ((img[x,y][1]*filt[4])+(img[x-1,y-1][1]*(filt[0]))+(img[x-1,y][1]*(filt[1]))+(img[x-1,y+1][1]*(filt[2]))+(img[x,y-1][1]*(filt[3]))+(img[x,y+1][1]*(filt[5]))+(img[x+1,y-1][1]*(filt[6]))+(img[x+1,y][1]*(filt[7]))+(img[x+1,y+1][1]*(filt[8])))/16

        temp3 = ((img[x,y][2]*filt[4])+(img[x-1,y-1][2]*(filt[0]))+(img[x-1,y][2]*(filt[1]))+(img[x-1,y+1][2]*(filt[2]))+(img[x,y-1][2]*(filt[3]))+(img[x,y+1][2]*(filt[5]))+(img[x+1,y-1][2]*(filt[6]))+(img[x+1,y][2]*(filt[7]))+(img[x+1,y+1][2]*(filt[8])))/16


        if temp1>255:
            temp1=255
        if temp2>255:
            temp2=255
        if temp3>255:
            temp3=255
        if temp1<0:
            temp1=0
        if temp2<0:
            temp2=0
        if temp3<0:
            temp3=0
        image1[x,y]=[temp1,temp2,temp3]
#image1 = image1.astype(np.uint8)
print(image1)
cv.imshow("filtered image",image1)
k = cv.waitKey(0)
