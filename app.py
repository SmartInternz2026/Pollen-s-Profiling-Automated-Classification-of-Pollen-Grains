from flask import Flask, render_template, request
import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import pickle

app = Flask(__name__)

MODEL_PATH = 'final_pollen_classifier_model.keras'
CLASS_INDICES_PATH = 'class_indices.pkl'

model = load_model(MODEL_PATH)
with open(CLASS_INDICES_PATH, 'rb') as f:
    class_indices = pickle.load(f)
index_to_class = {v: k for k, v in class_indices.items()}

@app.route('/', methods=['GET'])
def index():
    return render_template('main.html')

@app.route('/result', methods=['POST'])
def result():
    if 'file' not in request.files:
        return render_template('main.html', prediction="No file uploaded")
    file = request.files['file']
    if file.filename == '':
        return render_template('main.html', prediction="No file selected")
    if file:
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)
        try:
            img = image.load_img(file_path, target_size=(224, 224))
            img_array = image.img_to_array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)
            preds = model.predict(img_array)
            pred_idx = np.argmax(preds, axis=1)[0]
            pred_class = index_to_class.get(pred_idx, str(pred_idx))
            prediction = f"Predicted: {pred_class}"
        except Exception as e:
            prediction = f"Prediction error: {e}"
        os.remove(file_path)
        return render_template('main.html', prediction=prediction)
    return render_template('main.html', prediction="Error")

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)