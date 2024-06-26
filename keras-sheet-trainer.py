import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.datasets import mnist
from keras.utils import to_categorical
import keras

# Load the MNIST dataset
# (x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = np.load('training_images.npy')
y_train = np.load('training_labels.npy')

# x_train = x_train[1:500]
# y_train = y_train[1:500]

x_test = x_train[1:50]
y_test = y_train[1:50]


# Preprocess the data
x_train = x_train.reshape(x_train.shape[0], 120, 50, 3).astype('float32') / 255
x_test = x_test.reshape(x_test.shape[0], 120, 50, 3).astype('float32') / 255

# One-hot encode the target labels
# y_train = to_categorical(y_train)
# y_test = to_categorical(y_test)

# Define the model
model = Sequential()
model.add(keras.Input(shape=(120, 50, 3)))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5, batch_size=64, validation_data=(x_test, y_test))

model.save('first_model.keras')