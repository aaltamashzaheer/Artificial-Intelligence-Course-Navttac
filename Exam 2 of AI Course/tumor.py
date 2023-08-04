import numpy as np
import os
import cv2
from sklearn.model_selection import train_test_split
from keras.models import Model
from keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense

# Function to load MRI images and their corresponding labels
def load_data(data_dir):
    return np.array([cv2.resize(cv2.imread(os.path.join(data_dir, label_type, img_name)), (128, 128)) / 255.0
                     for label_type in os.listdir(data_dir) for img_name in os.listdir(os.path.join(data_dir, label_type))]), \
           np.array([1 if label == 'tumor' else 0 for label_type in os.listdir(data_dir) for label in os.listdir(os.path.join(data_dir, label_type))])

# Load the brain tumor dataset (assuming the dataset has 'tumor' and 'no_tumor' subdirectories)
data_dir = '/brain_tumor_dataset'
X, y = load_data(data_dir)

# One-hot encode the labels (e.g., 'tumor' -> [1, 0], 'no_tumor' -> [0, 1])
y = np.eye(2)[y]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build the multi-task CNN model
input_layer = Input(shape=(128, 128, 3))
conv1 = Conv2D(32, kernel_size=(3, 3), activation='relu')(input_layer)
maxpool1 = MaxPooling2D(pool_size=(2, 2))(conv1)
conv2 = Conv2D(64, kernel_size=(3, 3), activation='relu')(maxpool1)
maxpool2 = MaxPooling2D(pool_size=(2, 2))(conv2)
flatten = Flatten()(maxpool2)

# Task 1: Tumor classification
dense1 = Dense(128, activation='relu')(flatten)
output_tumor = Dense(2, activation='softmax', name='output_tumor')(dense1)

# Task 2: Tumor detection (binary classification)
dense2 = Dense(64, activation='relu')(flatten)
output_detection = Dense(1, activation='sigmoid', name='output_detection')(dense2)

# Define the multi-task model with two outputs
model = Model(inputs=input_layer, outputs=[output_tumor, output_detection])

# Compile the model with appropriate loss functions and metrics
model.compile(optimizer='adam',
              loss={'output_tumor': 'categorical_crossentropy', 'output_detection': 'binary_crossentropy'},
              metrics={'output_tumor': 'accuracy', 'output_detection': 'accuracy'})

# Train the multi-task model
model.fit(X_train, {'output_tumor': y_train, 'output_detection': y_train[:, 0]}, 
          validation_data=(X_test, {'output_tumor': y_test, 'output_detection': y_test[:, 0]}),
          epochs=10, batch_size=32)

# Evaluate the model
print("Tumor Classification Accuracy:", model.evaluate(X_test, {'output_tumor': y_test, 'output_detection': y_test[:, 0]})[3])
print("Tumor Detection Accuracy:", model.evaluate(X_test, {'output_tumor': y_test, 'output_detection': y_test[:, 0]})[4])