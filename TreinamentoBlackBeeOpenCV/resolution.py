import cv2 
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('imagens/lenna.png', -1)

print(img.shape[0])         #Index 0: Número de Linhas
print(img.shape[1])         #Index 1: Número de Colunas
print(img.shape[2])         #Index 2: Número de canais de cores

dst = cv2.resize(img, (50,50), interpolation = cv2.INTER_AREA)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.show()