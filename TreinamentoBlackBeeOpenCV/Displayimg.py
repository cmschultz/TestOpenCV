import cv2
import numpy as np

img = cv2.imread('imagens/lenna.png', 1)
img = cv2.resize(img, (400,400))  

cv2.imshow("Lenna", img)
cv2.waitKey()
cv2.destroyAllWindows()