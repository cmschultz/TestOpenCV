import numpy as np
import cv2

img = cv2.imread("./imagens/kuririn.jpg", 1)     # -1 == cv2.IMREAD_COLOR 
                                                 # Atenção que os dados são carregados em BGR ao invés de RGB
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_orange= np.array([10,100,100])
upper_orange= np.array([25,255,255])

mask = cv2.inRange(hsv, lower_orange, upper_orange)

result = cv2.bitwise_and(img, img, mask=mask)


cv2.imshow("Roupakuririn", result)               # Label/variável
cv2.waitKey(0)                                   # Espera o user apertar qq botão (key), se colocasse um numero 
                                                 # ali no lugar do (0) esperaria esse numero em segundos, NÃO É A KEY
cv2.destroyAllWindows()                          # Destroi as janelas após apertar qualquer botao.

