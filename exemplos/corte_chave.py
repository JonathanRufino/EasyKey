import numpy as np
import cv2
import matplotlib.pyplot as plt
import subprocess
import os

def load():
    im = cv2.imread('a2.jpg')
    os.system('convert a2.jpg -crop 150x315+185+118 +repage cp.jpg')
    img = cv2.imread('cp.jpg')
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(imgray, (5,5), 0)

    ret,t_antes = cv2.threshold(blur,127,255,0)
    t_depois = cv2.erode(t_antes, None, iterations=1)

    return (t_antes, t_depois)

if __name__ == '__main__':
    t_antes, t_depois = load()
    final = (t_antes - t_depois)
    final = (255-final)
