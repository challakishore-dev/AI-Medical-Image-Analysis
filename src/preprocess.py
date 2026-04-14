from tensorflow.keras.preprocessing.image import ImageDataGenerator

def get_generators():
    datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

    train = datagen.flow_from_directory(
        "data/chest_xray/train",
        target_size=(224,224),
        batch_size=8,
        class_mode='binary',
        subset='training'
    )

    val = datagen.flow_from_directory(
        "data/chest_xray/train",
        target_size=(224,224),
        batch_size=8,
        class_mode='binary',
        subset='validation'
    )

    return train, val
