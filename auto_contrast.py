import numpy as np
import cv2
import math
img=cv2.imread('images/low_contrast_1.jpg',cv2.IMREAD_GRAYSCALE)
height=img.shape[0]
width=img.shape[1]
min=255
max=0
for i in np.arange(height):
	for j in np.arange(width):
		a=img.item(i,j)
		if a>max:
			max=a
		if a<min:
			min=a
for i in np.arange(height):
	for j in np.arange(width):
		a=img.item(i,j)
		b=float(a-min)/(max-min)*255
		img.itemset((i,j),b)
cv2.imwrite('images/auto_contrast.jpg',img)
cv2.imshow('image',img)
cv2.waitkey(0)
cv2.destroyAllWindows()
