import cv2 
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('imagens/lenna.png', -1)

escala = 0.2
altura = int(escala*img.shape[0])        # É necessário usar um numero inteiro para pixels
largura = int (escala*img.shape[1])
dim = (largura, altura)

dst = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.show()