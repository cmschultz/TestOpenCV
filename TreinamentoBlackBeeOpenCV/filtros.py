import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../imagens/lenna.png')

blur = cv2.blur(img,(11,11))
median = cv2.medianBlur(img,11)
gaussian = cv2.GaussianBlur(img,(11,11), 0)

_, ax = plt.subplots()