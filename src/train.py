from src.preprocess import get_generators
from src.model import build_model

train, val = get_generators()
model = build_model()

model.fit(train, validation_data=val, epochs=2)

model.save("models/model.h5")
print("Training done")
