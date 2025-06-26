# Pollen's Profiling: Automated Classification of Pollen Grains

## Overview

This project is a Flask web application that uses a deep learning model to automatically classify pollen grain images. The model is trained using transfer learning (MobileNetV2) and can predict the pollen type from uploaded images.

## Features

- Upload pollen grain images via a web interface
- Automated image preprocessing and prediction
- Deep learning model trained on custom pollen dataset
- Results displayed instantly on the web page

## Project Structure

```
├── app.py                        # Flask web application
├── pollengrain.py                # Model training and export script
├── final_pollen_classifier_model.keras  # Trained Keras model
├── class_indices.pkl             # Class label mapping
├── templates/
│   └── main.html                 # Web UI template
├── uploads/                      # Temporary upload folder
├── static/                       # Static files (if any)
├── PollenGrains/                 # Example images
└── README.md                     # Project documentation
```

## How to Use

1. **Train the Model (if needed):**
   - Run `pollengrain.py` to train and export the model and class indices.
2. **Start the Flask App:**
   - Make sure `final_pollen_classifier_model.keras` and `class_indices.pkl` are in the project folder.
   - Run:
     ```bash
     python app.py
     ```
   - Open your browser at `http://127.0.0.1:5000/`
3. **Upload an Image:**
   - Use the web interface to upload a pollen grain image and see the predicted class.

## Requirements

- Python 3.10+
- Flask
- TensorFlow
- NumPy
- Pillow
- Pandas, scikit-learn, matplotlib (for training)

Install dependencies with:

```bash
pip install flask tensorflow numpy pillow pandas scikit-learn matplotlib
```

## Model Training

- The model is trained using MobileNetV2 as a base with custom dense layers.
- Data augmentation and early stopping are used for better generalization.
- After training, the model and class indices are saved for use in the Flask app.

## Credits

- Developed as part of the SmartInternz 2026 project.
- Dataset: Custom pollen grain images.

## License

This project is for educational and research purposes.
