import numpy as np
import cv2
from matplotlib import pyplot as plt

jpeg = cv2.imread('jpeg.jpg',0)

kernel = np.ones((2,3),np.uint8)

#erosion
jpegErode = cv2.erode(jpeg,kernel,iterations = 1)
		
#Dilation
jpegDilate = cv2.dilate(jpeg,kernel,iterations = 5)

#Opening
jpegOpening = cv2.morphologyEx(jpeg, cv2.MORPH_OPEN, kernel)

#Closing
jpegClosing = cv2.morphologyEx(jpeg, cv2.MORPH_CLOSE, kernel)

#show result
plt.subplot(2,3,1), plt.imshow(jpeg,'gray'), plt.title('Original')
plt.subplot(2,3,2), plt.imshow(jpegErode,'gray'), plt.title('Erosion')
plt.subplot(2,3,3), plt.imshow(jpegDilate,'gray'), plt.title('Dilation')
plt.subplot(2,3,4), plt.imshow(jpegOpening,'gray'), plt.title('Opening')
plt.subplot(2,3,5), plt.imshow(jpegClosing,'gray'), plt.title('Closing')
plt.savefig('morphological.jpg')
plt.show()