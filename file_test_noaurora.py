import glob
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def getRed(redVal):
    return '#%02x%02x%02x' % (redVal, 0, 0)

def getGreen(greenVal):
    return '#%02x%02x%02x' % (0, greenVal, 0)

def getBlue(blueVal):
    return '#%02x%02x%02x' % (0, 0, blueVal)


images = glob.glob("no-aurora/*.jpg")
for image in images:
    with open(image, 'rb') as file:
        img = Image.open(file)
        histogram = img.histogram()
        red_hist = histogram[0:256]
        blue_hist = histogram[256:512]
        green_hist = histogram[512:768]

# R histogram
plt.figure(0)
for i in range(0, 256):
    plt.bar(i, red_hist[i], color = getRed(i), edgecolor=getRed(i), alpha=0.3)


# G histogram
plt.figure(1)
for i in range(0, 256):
    plt.bar(i, green_hist[i], color = getGreen(i), edgecolor=getGreen(i),alpha=0.3)

# B histogram
plt.figure(2)
for i in range(0, 256):
    plt.bar(i, blue_hist[i], color = getBlue(i), edgecolor=getBlue(i),alpha=0.3)

plt.show()