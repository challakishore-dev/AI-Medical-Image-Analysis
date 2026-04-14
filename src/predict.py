import cv2
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model("models/model.h5")

def predict_image_array(img):
    img = cv2.resize(img, (224,224))
    img = img / 255.0
    img = np.reshape(img, (1,224,224,3))

    pred = model.predict(img)[0][0]
    return "PNEUMONIA" if pred > 0.5 else "NORMAL"
