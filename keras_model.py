import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
import numpy as np

# Step 1: Define your model
model = Sequential()
model.add(keras.Input(shape=(784,)))
model.add(Dense(64, activation='relu'))
model.add(Dense(10, activation='softmax'))

# Step 2: Compile your model
model.compile(optimizer=Adam(learning_rate=0.001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Step 3: Prepare your data (example with dummy data)
X_train = np.random.random((1000, 784))
y_train = np.random.randint(10, size=(1000,))
y_train = np.eye(10)[y_train]  # One-hot encoding

# Step 4: Train your model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

# Step 5: Evaluate your model
# Assuming you have separate validation data, use model.evaluate() here

# Step 6: Test your model
# Assuming you have separate test data, use model.evaluate() here