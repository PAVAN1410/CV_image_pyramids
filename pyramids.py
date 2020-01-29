import cv2
import numpy as np
img=cv2.imread(r'c:\Users\messi5.jpg')
#hr1=cv2.pyrUp(lr2)
#hr2=cv2.pyrUp(hr1)
cv2.imshow('img',img)
layer=img.copy()
gp=[layer]
#cv2.imshow('pyrup 1',hr1)
#cv2.imshow('pyrup 2',hr2)
for i in range(6):
    #lr=cv2.pyrDown(gp[i])
    #gp.append(lr)
    layer=cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow(str(i+1)+'gau',gp[i+1])
layer=gp[5]
cv2.imshow('upper level in gaussian pyramid',layer)
lap_pyr=[layer]
for i in range(5,0,-1):
    size=(gp[i-1].shape[1],gp[i-1].shape[0])
    gaussian_extend=cv2.pyrUp(gp[i],dstsize=size)
    laplacian=cv2.subtract(gp[i-1],gaussian_extend)
    #kernal=np.ones((5,5),np.uint8)
    #laplacian=cv2.dilate(laplacian,kernal)
    cv2.imshow(str(i)+'lap',laplacian)
    lap_pyr.append(laplacian)
            
cv2.waitKey(0)
cv2.destroyAllWindows()
