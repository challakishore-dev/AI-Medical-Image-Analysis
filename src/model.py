from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras import layers, models

def build_model():
    base = MobileNetV2(weights=None, include_top=False, input_shape=(224,224,3))
    base.trainable = True

    model = models.Sequential([
        base,
        layers.GlobalAveragePooling2D(),
        layers.Dense(64, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model
