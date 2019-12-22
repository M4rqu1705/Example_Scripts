#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import cv2

import tensorflow as tf
import tensorflow_hub as hub
from tensorflow.keras import layers

import time



IMAGE_RES = 224

def main():
    model = tf.keras.models.load_model('TRAINED KERAS MODEL.h5', custom_objects={'KerasLayer': hub.KerasLayer})
    model.trainable = False
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    class_names = {0: '3024 Plate 1x1', 1: '3004 Brick 1x2', 2: '3673 Peg 2M', 3: '3069 Flat Tile 1x2', 4: '18651 Cross Axle 2M with Snap friction', 5: '6632 Technic Lever 3M', 6: '3713 Bush for Cross Axle', 7: '3003 Brick 2x2', 8: '11214 Bush 3M friction with Cross axle', 9: '3040 Roof Tile 1x2x45deg', 10: '32123 half Bush', 11: '2357 Brick corner 1x2x2', 12: '3023 Plate 1x2', 13: '3794 Plate 1X2 with 1 Knob', 14: '3022 Plate 2x2', 15: '3005 Brick 1x1'}


    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        temp = np.array([cv2.resize(frame, dsize=(IMAGE_RES, IMAGE_RES), interpolation=cv2.INTER_CUBIC)])
        prediction = model.predict(temp)
        most_probable = np.argmax(prediction, axis=1)
        print(class_names[most_probable[0]])

        cv2.imshow('Video Capture',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

