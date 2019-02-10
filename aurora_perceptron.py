import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re

mu = 0.2
epochs = 5

plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Aurora perceptron learning")

np.random.seed(0)
initialBias = np.random.random()

# Read in data
data = []
with open('new.txt', 'rt') as in_file:
    for line in in_file:
        data.append(line.rstrip('\n'))

L = []
cols = []
for line in data:
    L.append(int(re.split(':', line)[0]))
    filtered = re.split("1:", line)[1].strip()
    cleanStr = filtered.replace('[', '')
    cleanStr2 = filtered.replace(']', '')
    cols_Str = cleanStr2.split(',')
    data_cols = [float(el) for el in cols_Str]
    cols.append(data_cols)




for j in range(epochs):
    accuracy = 0
    for i in range(rows):
        charge = W[0] + np.dot(data[i, 1:], W[1:])
        print(charge)
        predict = 1 if charge > 0 else 0
        if predict == L[i]:
            accuracy += 1
        else:
            Error = predict - L[i]
            W_t = W
            X_t = np.concatenate([1], data[i,1:])
            W_t = np.multiply(mu, np.multiply(Error, X_t))
            W = np.subtract(W, W_t)
            print(W_t)
            print("Error: %f charge: %f predict: %f L[i]: %f" % (Error, charge, predict, L[i]))
            plt.plot(np.arange(-5,5,0.1), -W/[0] / W[2] * np.arange(-5,5,0.1))
    print("Accuracy: %f" % (float(accuracy) / rows))
plt.show()