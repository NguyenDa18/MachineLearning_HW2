import numpy as np
import matplotlib.pyplot as plt
import glob
from PIL import Image

def getRed(redVal):
    return '#%02x%02x%02x' % (redVal, 0, 0)

def getGreen(greenVal):

    return '#%02x%02x%02x' % (0, greenVal, 0)

def getBlue(blueVal):

    return '#%02x%02x%02x' % (0, 0, blueVal)

plt.figure(0)
images = glob.glob('test/*.png')

# file = open("hist_vals.txt", "w")
perceptron_hist = []
for image in images:
    with open(image, 'rb') as file:
        img = Image.open(file)
        # get color histograms of img
        histogram = img.histogram()
        # Take only RGB counts
        l1 = histogram[0:256]
        red_hist = [val / max(l1) for val in l1]
        l2 = histogram[256:512]
        blue_hist = [val / max(l2) for val in l2]
        l3 = histogram[512:768]
        green_hist = [val / max(l3) for val in l3]
        rgb_hist = red_hist + green_hist + blue_hist
        perceptron_hist.append(rgb_hist)

with open('new.txt', 'w') as f:
    for hist in perceptron_hist:
        f.write("%s\n" % hist)
    f.close()

# R histogram

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
