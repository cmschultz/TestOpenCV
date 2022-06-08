import numpy as np
import cv2

cap = cv2.VideoCapture(0)           # Se houver mais de uma câmera é só mudar o numerozinho ali
                                    # além disso ele já rouba a câmera de outro recurso, caso esteja usando

while True:
    ret, frame = cap.read()         # Ret retorna false se outro programa já estiver usando a câmera, frame grava
    widgth = int(cap.get(3))        # get pega algumas propriedades numeradas de cap
    heigth = int(cap.get(4))

    # Considerando a imagem como um plano cartesiano, a sua origem (0,0) está no canto SUPERIOR esquerdo               
    img = cv2.line(frame, (0,0), (widgth, heigth), (255, 0, 0), 10)     # Desenha uma linha AZUL e 10 pixels, partindo da origem e 
                                                                        #cortando toda a diagonal do frame
    img = cv2.line(frame, (widgth,0), (0, heigth), (0, 0, 255), 10) 

    img = cv2.rectangle(frame, (100, 100), (200,200), (128,128,128), 5)  # O segundo e o terceiro parametro vão setar o inicio e o
                                                                         #fim da diagonal principal
    img = cv2.circle(img, (300, 300), 60, (0,255,0),-1)                  # O segundo parametro passa as coordenadas do centro
                                                                         #e a terceira é o seu raio. Ou seja, o diâmetro, quando
                                                                         #olhado na horizontal vai de 240 a 360.
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'Alguma coisa importante.', (10, heigth - 10), font, 1, (0,0,0), 5, cv2.LINE_AA)


    cv2.imshow('frame', img)      #se escreve frame ou cap.read() no segundo paraâmetro sai a captura ao vivo

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()                       # deixa a câmera a disposição do pc dnv, caso tenha roubado ele devolve
cv2.destroyAllWindows()         