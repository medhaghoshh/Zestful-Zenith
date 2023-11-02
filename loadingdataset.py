#importing modules
import tensorflow as t
import numpy as np
import os
import sys
import cv2
import matplotlib.pyplot as pp
import pickle
import random
import pandas as pd
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense,Dropout,Flatten,Conv2D,MaxPooling2D,Input
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import RMSprop
import pickle
import matplotlib.pyplot as pp
from sklearn.model_selection import train_test_split

data_dir= "C:/Users/ayush/Desktop/ZZ/modeldaataload/"
a =["tullsi","neeem"]
for category in a:
    path= os.path.join(data_dir, category) #path to tulsi or neem dir
    for img in os.listdir(path):
        img_array= cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
        pp.imshow(img_array, cmap="gray")
        pp.show()
        pp.waitKey(0)
        break
    break    
img_size= 128
new_array = cv2.resize(img_array,(img_size, img_size))
pp.imshow(new_array, cmap='gray')
pp.show()
training_data= []

def create_training_data():
    for category in a:
            path= os.path.join(data_dir, category) #path to tulsi or neem dir
            classs= a.index(category)
            for img in os.listdir(path):
                try:
                    img_array= cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
                    new_array = cv2.resize(img_array,(img_size, img_size))
                    training_data.append([new_array,classs])
                except Exception as e:
                    pass
                
                
create_training_data()    

print(len(training_data))
random.shuffle(training_data)

# Split the data into features and labels
X = []
y = []

for features, label in training_data:
    X.append(features)
    y.append(label)

# Normalizing the pixel values
X = np.array(X) / 255.0

# Spliting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Reshaping input data to have 4 dimensions
X_train = X_train.reshape(-1, 128, 128, 1)
y_train = np.array(y_train)
