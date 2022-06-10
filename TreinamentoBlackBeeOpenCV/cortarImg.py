import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
import IPython.display as display

img = cv.imshow('imagens/lenna.jpg', -1)

@interact(y=widgets.IntSlider(min=0,max=300), x=widgets.IntSlider(min=0,max=300))
def f(y,x):
    cut = img[y:y+2000, x:x+2000]
    plt.imshow(cv.cvtColor(cut, cv.COLOR_BGR2RGB))
    plt.show()

w = widgets.IntSlider()
display(w)