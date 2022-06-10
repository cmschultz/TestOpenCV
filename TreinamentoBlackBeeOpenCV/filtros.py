import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('imagens/lenna.png')

blur = cv2.blur(img,(11,11))
median = cv2.medianBlur(img,11)
gaussian = cv2.GaussianBlur(img,(11,11), 0)

_, ax = plt.subplots(1, 4, figsize=(12, 12), sharex=True, sharey=True) 

ax[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
ax[1].imshow(cv2.cvtColor(blur, cv2.COLOR_BGR2RGB))
ax[2].imshow(cv2.cvtColor(median, cv2.COLOR_BGR2RGB))
ax[3].imshow(cv2.cvtColor(gaussian, cv2.COLOR_BGR2RGB))

ax[0].set_title("Original")
ax[1].set_title("Filtro de Média")
ax[2].set_title("Filtro de Mediana")
ax[3].set_title("Filtro Gaussiano")

for a in ax:
    a.set_axis_on()

plt.show()