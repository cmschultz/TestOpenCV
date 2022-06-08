import numpy as np
import cv2

cap = cv2.VideoCapture(0)           # Se houver mais de uma câmera é só mudar o numerozinho ali
                                    # além disso ele já rouba a câmera de outro recurso, caso esteja usando

while True:
    ret, frame = cap.read()         # Ret retorna false se outro programa já estiver usando a câmera, frame grava
    widgth = int(cap.get(3))        # get pega algumas propriedades numeradas de cap
    heigth = int(cap.get(4))

    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    image[:heigth//2, :widgth//2] = cv2.rotate(smaller_frame,cv2.ROTATE_180)
    image[heigth//2:, :widgth//2] = smaller_frame
    image[:heigth//2, widgth//2:] = smaller_frame
    image[heigth//2:, widgth//2:] = cv2.rotate(smaller_frame,cv2.ROTATE_180)

    cv2.imshow('frame', image)      #se escreve frame ou cap.read() no segundo paraâmetro sai a captura ao vivo

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()                       # deixa a câmera a disposição do pc dnv, caso tenha roubado ele devolve
cv2.destroyAllWindows()         