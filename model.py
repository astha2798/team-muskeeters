import cv2
import dlib
import os
import numpy as np
from PIL import Image
import glob
from pylab import *
import scipy.io

folder = "/home/palak/Desktop/hack/data/"
predictor_path = "/home/palak/Desktop/hack/shape_predictor_68_face_landmarks(1).dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)

i=0
for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
#       img = np.array(img)
#       s = img.shape
#       print(s)
        print(i)
        i = i+1
        dets = detector(img, 1)
        print("Number of faces detected: {}".format(len(dets)))
        if(len(dets) > 0):
            for k, d in enumerate(dets):
                print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(k, d.left(), d.top(), d.right(), d.bottom()))
                x = d.left()
                y = d.top()
                w = d.right() - x
                h = d.bottom() - y
                crop_img = img[y:y+h, x:x+w]
                cv2.imwrite('/home/palak/Desktop/hack/faces/{}.jpg'.format(filename), crop_img)  

from resizeimage import resizeimage
face_path = "/home/palak/Desktop/hack/faces/"
x=[]
for filename in os.listdir(face_path):
    img1 = Image.open(os.path.join(face_path,filename))
    new1 = resizeimage.resize_contain(img1, [223, 223, 3])
    new1 = np.array(new1, dtype='uint8')
    x.append(new1)
x = np.array(x)
print(x.shape)

import csv
from keras.utils import np_utils

csv_file=open("/home/palak/Desktop/hack/datanew.csv", "r")
reader = csv.reader(csv_file)

labels=[]
for row in reader:
    label=row[1:2]
    labels.append(label)
    
y = np_utils.to_categorical(labels, 8)

import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.layers.normalization import BatchNormalization
from keras.callbacks import TensorBoard


model= Sequential()

model.add(Conv2D(96, kernel_size=(11, 11), strides=(4, 4), activation="relu", input_shape=(223, 223, 3)))
model.add(MaxPooling2D(pool_size=(3, 3), strides=(2, 2)))
model.add(BatchNormalization())

model.add(Conv2D(256, kernel_size=(5, 5), activation="relu"))
model.add(MaxPooling2D(pool_size=(3, 3), strides=(2, 2)))
model.add(BatchNormalization())

model.add(Conv2D(256, kernel_size=(3, 3), activation="relu"))
model.add(Conv2D(384, kernel_size=(3, 3), activation="relu"))
model.add(Conv2D(384, kernel_size=(3, 3), activation="relu"))
model.add(MaxPooling2D(pool_size=(3, 3), strides=(2, 2)))
model.add(BatchNormalization())

model.add(Flatten())
model.add(Dense(4096, activation="tanh"))
model.add(Dropout(0.5))
model.add(Dense(4096, activation="tanh"))
model.add(Dropout(0.5))

model.add(Dense(8, activation="softmax"))

model.summary()

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(x, y, batch_size=64, epochs=70, verbose=1, validation_split=0.1, shuffle=True)
