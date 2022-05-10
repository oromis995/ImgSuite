import numpy as np
import cv2
from numpy import asarray
from PIL import Image
import sys
np.set_printoptions(threshold=sys.maxsize)
image = Image.open("Intro.png")
numpydata = asarray(image)
print(numpydata)
image = Image.fromarray(numpydata)
image.show()
b, g, r, h = cv2.split(numpydata)
print(b, g, r)
