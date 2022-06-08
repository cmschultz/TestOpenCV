import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if (cap.isOpened()== False):
  print("Error opening video stream or file")

while(cap.isOpened()):
    ret, frame = cap.read()             #ret: valor booleano que indica se o frame está disponível
                                        #frame: ecebe o próximo frame do vídeo          
    if ret:
        cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()