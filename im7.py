import numpy as np
import cv2
import math
import histogram as h
import cumulative_histogram as ch
img=cv2.imread('images/image1.jpg',cv2.IMREAD_GRAYSCALE)
img_ref=cv2.imread('images/cat.jpg',cv2.IMREAD_GRAYSCALE)
height_ref=img_ref.shape[0]
width_ref=img_ref.shape[1]
pixels_ref=width_ref*height_ref
hist=h.histogram(img)
hist_ref=h.histogram(img_ref)
cum_hist=ch.cumulative_histogram(hist)
cum_hist_ref=ch.cumulative_histogram(hist_ref)
prob_cum_hist=cum_hist/pixels
prob_cum_hist_ref=cum_hist_ref/pixels_ref
k=256
new_values=np.zeros((k))
for a in np.arange(k):
	j=k-1
	while true:
		new_values[a]=j
		j=j-1
		if j<0 or prob_cum_hist[a]>prob_cum_hist_ref[j]
			break
for i in np.arange(height):
	for j in np.arange(width):
		a=img.item(i,j)
		b=new_values[a]
		img.items((i,j),b)
cv2.imwrite('images/modified_auto_contrast.jpg',img)
cv2.imshow('image',img)
cv2.waitkey(0)
cv2.destroyAllWindows()




