import numpy as np
import pandas as pd
import math


# Function of Sigmoid, transfer data into range of 0~1
def Sigmoid(z):
    x = 1 / (1 + np.exp(-z))
    return x


# Function of predict, project all labels into binary labels
def predict(prediction, weight):
    wx = np.dot(prediction, weight)
    for i in range(len(wx)):
        wx[i] = Sigmoid(wx[i])
    return wx


# Function of cost, used for the calculation of average cost
def cost(features, labels, weights):
    wx = predict(features, weights)

    for i in range(len(wx)):
        print((-labels * np.log(wx[i])))
        print((1 - labels) * np.log(1 - wx[i]))
        cost_function_result = (-labels * np.log(wx) - (1 - labels) * np.log(1 - wx[i]))
    print(cost_function_result)
    print(wx)
    cost = np.sum(cost_function_result) / len(cost_function_result)
    return cost


prediction = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 1], [2, 3, 1, 2, 3]]  # 3x5
prediction = np.array(prediction)
weight = [0.5, 1, 0.4, 1, 0.5]  # 5X1
weight = np.array(weight)
weight = np.array(weight)
weight = weight.transpose()
labels = [0, 1, 1]
labels = np.array(labels)
print(labels)
Predictin_final = predict(prediction, weight)
# print(Predictin_final)
Cost = cost(prediction, labels, weight)
print(Cost)
