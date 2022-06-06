import cv2
                                                
img = cv2.imread("./imagens/kuririn.jpg", 1)     # -1 == cv2.IMREAD_COLOR 
                                                 # Atenção que os dados são carregados em BGR ao invés de RGB
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)     # altera o tamanho para a metade
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imwrite('newKuririn.jpg', img)

cv2.imshow("kuririn", img)                       # Label/variável
cv2.waitKey(0)                                   # Espera o user apertar qq botão (key), se colocasse um numero 
                                                 # ali no lugar do (0) esperaria esse numero em segundos, NÃO É A KEY
cv2.destroyAllWindows()                          # Destroi as janelas após apertar qualquer botao.

