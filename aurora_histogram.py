import numpy as np
import matplotlib.pyplot as plt
import glob
import re
from PIL import Image

def getRed(redVal):
    return '#%02x%02x%02x' % (redVal, 0, 0)

def getGreen(greenVal):
    return '#%02x%02x%02x' % (0, greenVal, 0)

def getBlue(blueVal):
    return '#%02x%02x%02x' % (0, 0, blueVal)

def genHist(images):
    perceptron_hist = []
    for image in images:
        with open(image, 'rb') as file:
            img = Image.open(file)
            # get color histograms of img
            histogram = img.histogram()
            # Take only RGB counts
            l1 = histogram[0:256]
            red_hist = [val / 1500 for val in l1]
            red_hist = [1 if val > 1 else val for val in red_hist]
            l2 = histogram[256:512]
            blue_hist = [val / 1800 for val in l2]
            blue_hist = [1 if val > 1 else val for val in blue_hist]
            l3 = histogram[512:768]
            green_hist = [val / 2500 for val in l3]
            green_hist = [1 if val > 1 else val for val in green_hist]
            rgb_hist = red_hist + green_hist + blue_hist
            perceptron_hist.append(rgb_hist)

    # R histogram
    plt.figure(0)
    # for i in range(0, 256):
    #     plt.bar(i, red_hist[i], color = getRed(i), edgecolor=getRed(i), alpha=0.3)


    # # G histogram
    # plt.figure(1)
    # for i in range(0, 256):
    #     plt.bar(i, green_hist[i], color = getGreen(i), edgecolor=getGreen(i),alpha=0.3)

    # # B histogram
    # plt.figure(2)
    # for i in range(0, 256):
    #     plt.bar(i, blue_hist[i], color = getBlue(i), edgecolor=getBlue(i),alpha=0.3)
    return perceptron_hist

aurora_images = glob.glob('yes-aurora/*.jpg')
no_aurora_images = glob.glob('no-aurora/*.jpg')

aurora_hist = genHist(aurora_images)
no_aurora_hist = genHist(no_aurora_images)

with open('new.txt', 'w') as f:
    for item in aurora_hist:
        f.write("1:")
        f.write("%s\n" % item)
    for item in no_aurora_hist:
        f.write("-1:")
        f.write("%s\n" % item)
    f.close()

plt.show()


