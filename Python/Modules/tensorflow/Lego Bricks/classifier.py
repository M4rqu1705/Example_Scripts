#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_datasets as tfds
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import numpy as np
import matplotlib.pyplot as plt
import os

import pickle


# Constants throughout this program
IMAGE_RES = 224
BATCH_SIZE = 32
TRAINED_LEARNING_MODEL_URL = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4"
EPOCHS = 3


def get_processed_data():
    train_folder = "./LEGO brick images/train"
    validation_folder = "./LEGO brick images/valid"

    image_gen_train = ImageDataGenerator(
            rescale=1./255,
            rotation_range=40,
            width_shift_range=0.2,
            height_shift_range=0.2,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True,
            fill_mode='nearest')

    train_data_gen = image_gen_train.flow_from_directory(directory=train_folder,
            target_size=(IMAGE_RES, IMAGE_RES),
            color_mode='rgb',
            classes=os.listdir(train_folder),
            class_mode='sparse',
            batch_size=BATCH_SIZE,
            shuffle=True)

    image_gen_val = ImageDataGenerator(rescale=1./255)

    val_data_gen = image_gen_val.flow_from_directory(directory=validation_folder,
            target_size=(IMAGE_RES, IMAGE_RES),
            color_mode='rgb',
            classes=os.listdir(validation_folder),
            class_mode='sparse',
            batch_size=BATCH_SIZE,
            shuffle=True)

    info = {
            'labels':train_data_gen.class_indices,
            'num_labels':train_data_gen.num_classes,
            'num_training':train_data_gen.n,
            'num_validation':train_data_gen.n
            }


    return train_data_gen, val_data_gen, info

def main():

    # Retrieve processed data 
    training_set, validation_set, dataset_info = get_processed_data()

    # Count how many labels, training examples and validation examples there are
    num_classes = dataset_info.get('num_labels')
    num_training_examples = dataset_info.get('num_training')
    num_validation_examples = dataset_info.get('num_validation')

    class_ids = dataset_info.get('labels')
    class_names = dict()
    for key in class_ids:
        value = class_ids[key]
        class_names[value] = key

    # Format_image function to 'normalize' these into IMAGE_RES square and with values from 0 to 1
    def format_image(image, label):
        image = tf.image.resize(image, (IMAGE_RES, IMAGE_RES))/255.0
        return image, label

    # Prepare freezed feature extractor from trained learning model we want to use
    feature_extractor = hub.KerasLayer(TRAINED_LEARNING_MODEL_URL, input_shape=(IMAGE_RES, IMAGE_RES, 3), trainable=False)

    # Early stopping callback to prevent overfitting
    # Thanks https://www.youtube.com/watch?v=-vHQub0NXI4
    early_stop = tf.keras.callbacks.EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=2)

    model = tf.keras.Sequential([
        feature_extractor,
        tf.keras.layers.Dense(num_classes, activation='softmax')
        ])


    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    history = model.fit(training_set, epochs=EPOCHS, validation_data=validation_set)

    fileObject = open("trainedModelPickle", 'wb')
    pickle.dump(model, fileObject)
    fileObject.close()

    tf.saved_model.save(model, ".\\TRAINED MODEL")


    # Graph data
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']

    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs_range = range(EPOCHS)

    plt.figure(figsize=(8, 8))
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, acc, label='Training Accuracy')
    plt.plot(epochs_range, val_acc, label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.title('Training and Validation Accuracy')

    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, loss, label='Training Loss')
    plt.plot(epochs_range, val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.title('Training and Validation Loss')
    plt.show()

    # Extract images and labels with which to make predictions
    image_batch, label_batch = next(iter(train_batches))
    image_batch, label_batch = image_batch.numpy(), label_batch.numpy()

    # Make prediction
    predicted_batch = model.predict(image_batch)
    predicted_ids = np.argmax(predicted_batch, axis=-1)
    predicted_class_names = class_names[predicted_ids]

    # Plot model predictions
    plt.figure(figsize=(10,9))
    for n in range(30):
        plt.subplot(6,5,n+1)
        plt.subplots_adjust(hspace = 0.3)
        plt.imshow(image_batch[n])
        color = "blue" if predicted_ids[n] == label_batch[n] else "red"
        plt.title(predicted_class_names[n].title(), color=color)
        plt.axis('off')
    _ = plt.suptitle("Model predictions (blue: correct, red: incorrect)")


if __name__ == "__main__":
    main()
