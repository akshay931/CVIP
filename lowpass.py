import cv2 as cv

img = cv.imread('plane.tiff')
row,col,channel = img.shape
cv.imshow("image",img)

# 3x3 default filter applied
for x in range(0,row-1):
    for y in range(0,col-1):
        temp1 = img[x,y][0]/9+img[x-1,y-1][0]/9+img[x-1,y][0]/9+img[x-1,y+1][0]/9+img[x,y-1][0]/9+img[x,y+1][0]/9+img[x+1,y-1][0]/9+img[x+1,y][0]/9+img[x+1,y+1][0]/9

        temp2 = img[x,y][1]/9+img[x-1,y-1][1]/9+img[x-1,y][1]/9+img[x-1,y+1][1]/9+img[x,y-1][1]/9+img[x,y+1][1]/9+img[x+1,y-1][1]/9+img[x+1,y][1]/9+img[x+1,y+1][1]/9
        temp3 = img[x,y][2]/9+img[x-1,y-1][2]/9+img[x-1,y][2]/9+img[x-1,y+1][2]/9+img[x,y-1][2]/9+img[x,y+1][2]/9+img[x+1,y-1][2]/9+img[x+1,y][2]/9+img[x+1,y+1][2]/9
        img[x,y]=[temp1,temp2,temp3]

cv.imshow("filtered image",img)


k = cv.waitKey(0)
