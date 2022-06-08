import numpy as np
import cv2

image = cv2.imread('imagens\kuririn.jpg')

alpha = 1.5 # Contrast control (1.0-3.0)
beta = 0 # Brightness control (0-100)

adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

cv2.imshow('original', image)
cv2.imshow('adjusted', adjusted)
cv2.waitKey()
cv2.destroyAllWindows()

# lower_blue= np.array([35,140,60])
# upper_blue= np.array([255,255,180])

# mask = cv2.inRange(hsv, lower_blue, upper_blue)

# result = cv2.bitwise_and(img, img, mask=mask)


# cv2.imshow("Roupakuririn", result)               # Label/variável
# cv2.waitKey(0)                                   # Espera o user apertar qq botão (key), se colocasse um numero 
#                                                  # ali no lugar do (0) esperaria esse numero em segundos, NÃO É A KEY
# cv2.destroyAllWindows()                          # Destroi as janelas após apertar qualquer botao.

