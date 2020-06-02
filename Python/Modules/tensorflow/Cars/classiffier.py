import sys, io
# Suppresss any output
#  text_trap = io.StringIO()
#  sys.stdout = text_trap
#  sys.stderr = text_trap

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt


def getProcessedData():
    # Retrieve file line by line
    data = []
    with open("car.data") as temp:
        data = temp.readlines()

    # Process data ...

    # Split into multi-dimensional list
    data = [x.strip().lower().split(',') for x in data]
    # Extract labels
    labels = [x.pop() for x in data]

    # Substitute each criteria for key numbers ...
    classes = {"unacc":0, "acc":1, "good":2, "vgood":3}
    price = {"vhigh":0, "high":1, "med":2, "low":3}
    maint = {"vhigh":0, "high":1, "med":2, "low":3}
    doors = {"2":0, "3":1, "4":2, "5more":3}
    persons = {"2":0, "4":1, "more":2}
    lug_boot = {"small":0, "med":1, "big":2}
    safety = {"low":0, "med":1, "high":2}

    labels = [classes[x] for x in labels]
    for item in data:
        item[0] = price[item[0]]
        item[1] = maint[item[1]]
        item[2] = doors[item[2]]
        item[3] = persons[item[3]]
        item[4] = lug_boot[item[4]]
        item[5] = safety[item[5]]

    return labels, data

def separateData(labels, data, trainPct):
    # Identify point where to divide
    div = round(len(labels) * trainPct)
    return (labels[:div], data[:div]), (labels[div:], data[div:])


def main():


    labels, data = getProcessedData()
    (trainLabels, trainData), (testLabels, testData) = separateData(labels,
            data, 0.9) 

    # Convert to numpy arrays
    trainLabels = np.array(trainLabels)
    trainData = np.array(trainData)
    testLabels = np.array(testLabels)
    testData = np.array(testData)

    accuracies = []
    for c in range(10):
        model = keras.Sequential([
            keras.layers.Dense(16, input_shape=(6,), activation="relu"),
            keras.layers.Dense(32, activation="relu", use_bias=False),
            keras.layers.BatchNormalization(),
            keras.layers.Dense(128, activation="relu"),
            keras.layers.Dense(16, activation="relu"),
            keras.layers.Dense(4, activation="softmax")
            ])

        model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

        model.fit(trainData, trainLabels, epochs=9)

        test_loss, test_acc = model.evaluate(testData, testLabels)
        accuracies.append(test_acc)

    # Enable output to standard input again
    sys.stdout = sys.__stdout__

    # Print average of accuracies
    print(sum(accuracies)/len(accuracies))

    '''
    predictions = model.predict(testData)
    for c in range(10):
        prediction = np.argmax(predictions[c])
        print("True Label: {}, Predicted Label: {}, Data:".format(
                    testLabels[c],
                    prediction
                    ), end=' '
                )
        print(testData[c])
        '''

if __name__ == "__main__":
    main()

# Thank you https://archive.ics.uci.edu/ml/machine-learning-databases/car/ for
# the data, and thank you
# https://www.quora.com/Given-a-feedforward-NN-with-low-training-accuracy-thus-low-test-accuracy-how-can-I-improve-the-training-accuracy-and-hopefully-the-test-accuracy
# for the recommendations
