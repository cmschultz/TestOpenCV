import cv2
import random

img = cv2.imread('imagens/kuririn.jpg', -1)

# print(img)
# print(type(img))
# print(img.shape)                             # number of rows/ number of columns / number of channels


# print(img[257][45:400])

for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]

cv2.imshow('kuririn', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# O código dai de cima troca os pixels das 100 primeiras linhas por cores aleatórias

tag = img[500:700, 600:900]                     #deixa no jeito esse slice da img

