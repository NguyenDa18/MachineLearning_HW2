import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re

mu = 0.001
epochs = 10
batch_size = 200

# Part 3.
# Build a simple perceptron with a step activation function. The perceptron should take the color histogram as its input and return a single output: 1 if aurora is in the image and 0 otherwise. You can implement this logic by simple checking the perceptron’s output, if the output is high return true, otherwise return false. When you are training the perceptron split the feature vectors into 80% of images for training and reserve 20% for validation. When training the perceptron, present the color histograms at random. Test different batch sizes (20 would be a good start).

# Make sure your perceptron implementation has a parameterized learning rate. Perform experiments with the learning m = 0.1, 0.01, 0.001, and 1.5. Run as many learning batches/epochs as you need to achieve desired classification performance. For your report, one of your figures should include a plot of a training error and classification accuracy (two plot curves) vs. training epoch. You might also want to include accuracy, precision, recall measures for your experiments.


plt.title("Aurora perceptron learning, " + ' Batch Size: ' + str(batch_size) + ', ' + str(epochs) + ' epochs' + ', Mu: ' + str(mu))
plt.xlabel("Epoch")
plt.ylabel("Accuracy")

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

# data = np.array([[1,1,1],
#                  [1,1,2],
#                  [0,2,-2],
#                  [0,-2,-1],
#                  [0,-1,-2],
#                  [1,-2,1],
#                  [1,-1,1]])

L = data[:,0] # labels of samples

# Generate random weights of 256 + 256 + 256 AND 1 for initial bias
W = np.random.random_sample((256 * 3) + 1,) - np.random.random_sample()
# W = np.array([0, 1, 0.5])


rows = data.shape[0]
cols = data.shape[1]

############################################################
                    ## PERCEPTRON ##
############################################################
total_accuracy = []
current_accuracy = 0
for j in range(epochs):
    accuracy = 0
    total_accuracy.append(current_accuracy)
    for i in range(batch_size):
        charge = W[0] + np.dot(data[i, 1:], W[1:])
        print('i: %d' % i)
        print("Charge: %f" % charge)
        predict = 1 if charge > 0 else 0
        print("Predict: %d" % predict)

        if predict == L[i]:
            accuracy += 1
        else:
            Error = predict - L[i]
            W_t = W
            X_t  = np.concatenate(([1], data[i,1:]))
            W_t = np.multiply(mu, np.multiply(Error, X_t))
            W = np.subtract(W, W_t)
            print("Error: %f charge: %f predict: %f L[i]: %f" % (Error, charge, predict, L[i]))
            current_accuracy = float(accuracy) / batch_size
            # plt.plot (np.arange (-2.5,2.5,0.1), -W[0]/W[2] - W[1]/W[2] * np.arange(-2.5,2.5,0.1))
    print("Epoch: %d" % j)
    print("Accuracy: %f" % (float(accuracy) / batch_size))

for count, value in enumerate(total_accuracy):
    # print("Epoch: %d, Error: %f" % (count, value))
    plt.scatter(count, value)
plt.show()