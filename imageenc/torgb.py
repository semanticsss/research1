import cv2
import numpy as np

def torgb(image):
    newimage = cv2.imread(image)

    if newimage is not None:
        img_rgb = cv2.cvtColor(newimage, cv2.COLOR_BGR2RGB)
        return img_rgb

