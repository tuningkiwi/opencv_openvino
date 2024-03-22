import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

mnist = tf.keras.datasets.fashion_mnist
(image_train, label_train), (image_test, label_test) = mnist.load_data()

print("Train Image shape : ", image_train.shape)
print("Train Label : ", label_train, "\n")
print(image_train[0])

NUM = 20
plt.figure(figsize=(15, 15)) 
for idx in range(NUM):
    plt.subplot(5, 5, idx+1) 
    plt.imshow(image_train[idx], cmap='gray')
    plt.title(f'Label: {label_train[idx]}')
plt.show()

model = tf.keras.Sequential()
model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(tf.keras.layers.MaxPooling2D((2, 2)))
model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu'))
model.add(tf.keras.layers.MaxPool2D(2, 2))
model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu'))
model.add(tf.keras.layers.MaxPool2D(2, 2))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation='sigmoid'))
model.add(tf.keras.layers.Dense(64, activation='sigmoid'))
model.add(tf.keras.layers.Dense(32, activation='sigmoid'))
model.add(tf.keras.layers.Dense(10, activation='softmax'))

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'], 
)

model.fit(image_train, label_train, epochs=10, batch_size=10)
model.summary()
model.save('ANN_mnist.h5')

NUM = 5
predict = model.predict(image_test[0:NUM])
print(predict)
print(" * Prediction", np.argmax(predict, axis=1))

plt.figure(figsize=(15, 15))
for idx in range(NUM):
    sp = plt.subplot(1, 5, idx+1)
    plt.imshow(image_test[idx])
plt.show()

