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

# Read in data
lines_data = []
with open('new.txt', 'rt') as in_file:
    for line in in_file:
        lines_data.append(line.rstrip('\n'))

data_list = []
for line in lines_data:
    label = int(re.split(':', line)[0])

    parsed_input = re.split('1:', line)[1].strip()
    parsed_input = parsed_input.replace("[", "")
    parsed_input = parsed_input.replace("]", "")
    parsed_input_list = parsed_input.split(',')
    inputs = [float(el) for el in parsed_input_list]
    row = [label] + inputs
    data_list.append(row)
data = np.asarray(data_list)

L = data[:,0] # labels of samples

# Generate random weights of 256 + 256 + 256 AND 1 for initial bias
W = np.random.random_sample((256 * 3) + 1,)

rows = data.shape[0]
cols = data.shape[1]

############################################################
                    ## PERCEPTRON ##
############################################################
for j in range(epochs):
    accuracy = 0
    for i in range(rows):
        charge = W[0] + np.dot(data[i, 1:], W[1:])
        print("Charge: %f" % charge)
        predict = 1 if charge > 0 else 0
        if predict == L[i]:
            accuracy += 1
        else:
            Error = predict - L[i]
            W_t = W
            # X_t = np.concatenate([1.000000000000], data[i, 1:])
            W_t = np.multiply(mu, np.multiply(Error, data[i, 1:]))
            W = np.subtract(W, W_t)
            print(W_t)
            print("Error: %f charge: %f predict: %f L[i]: %f" % (Error, charge, predict, L[i]))
            plt.plot(np.arange(-5,5,0.1), -W/[0] / W[2] * np.arange(-5,5,0.1))
    print("Accuracy: %f" % (float(accuracy) / rows))
plt.show()