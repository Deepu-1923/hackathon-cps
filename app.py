from flask import Flask, request, jsonify
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

app = Flask(__name__)
model = load_model("image_model.h5")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["image"].read()
    npimg = np.frombuffer(file, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    prediction = model.predict(img)
    response = f"Detected object: {prediction.argmax()}"
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
