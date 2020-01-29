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
    #cv2.imshow(str(i+1)+'gau',gp[i+1])
layer=gp[5]
cv2.imshow('upper level in gaussian pyramid',layer)
lap_pyr=[layer]
for i in range(5,0,-1):
    size=(gp[i-1].shape[1],gp[i-1].shape[0])
    gaussian_extend=cv2.pyrUp(gp[i],dstsize=size)
    laplacian=cv2.subtract(gp[i-1],gaussian_extend)
    #kernal=np.ones((
    
  (laplacian,kernal)

#for reconstruction    
reconstruct_image=lap_pyr[0]


for i in range(1,6):
    size=(lap_pyr[i].shape[1],lap_pyr[i].shape[0])
    reconstruct_image=cv2.pyrUp(reconstruct_image,dstsize=size)
    reconstruct_image=cv2.add(reconstruct_image,lap_pyr[i])
    cv2.imshow(str(i),reconstruct_image)
    
cv2.waitKey(0)
cv2.destroyAllWindows()
