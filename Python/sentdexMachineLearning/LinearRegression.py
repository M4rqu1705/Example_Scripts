#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import quandl
import numpy as np
from sklearn import preprocessing, model_selection
from sklearn.linear_model import LinearRegression

def main():
    # Get data from quandl
    data = quandl.get('WIKI/GOOGL')

    # Only preserve relevant data
    dataframe = data[[
        'Adj. Open',
        'Adj. High',
        'Adj. Low',
        'Adj. Close',
        'Adj. Volume'
    ]]

    # Prepare High-Low ~percentage of error
    dataframe['HL_percent'] = (dataframe['Adj. High'] - dataframe['Adj. Low']) / dataframe['Adj. Low'] * 100.0
    # Prepare Open-Close ~percentage of error
    dataframe['OC_percent'] = (dataframe['Adj. Close'] - dataframe['Adj. Open']) / dataframe['Adj. Open'] * 100.0

    # What column are we going to forecast?
    forecast_column = 'Adj. Close'
    # How many days forward are we going to forecast?
    forecast_out = 30

    dataframe.fillna(-99999, inplace=True)

    # Prepare label column with according data
    dataframe['label'] = dataframe[forecast_column].shift(-forecast_out)
    dataframe.dropna(inplace=True)

    # Prepare features and label datasets
    X = np.array(dataframe.drop(['label'], 1))  # Make a copy without label column
    X = preprocessing.scale(X)                  # Scale for faster computation
    y = np.array(dataframe['label'])            # Only use label column

    # Extract train and test samples
    X_train, X_test, y_train, y_test =
        model_selection.train_test_split(X, y, test_size=0.2)

    # Train and test data
    classificator = LinearRegression()
    classificator.fit(X_train, y_train)
    accuracy = classificator.score(X_test, y_test)

    print(accuracy)



if __name__ == "__main__":
    main()

