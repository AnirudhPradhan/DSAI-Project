from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

app = Flask(__name__)

model = load_model('your_model.h5') 

@app.route('/predict', methods=['POST'])
def predict(image_path):
    try:
        img = load_img(image_path, target_size=(224, 224))  
        img_array = img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255  
    except Exception as e:
        print(f"Failed to load image: {e}")
        return None
    
    try:
        predictions = model.predict(img_array)
    except Exception as e:
        print(f"Failed to make prediction: {e}")
        return None
    
    predicted_class = np.argmax(predictions)
    
    if predicted_class == 0:
        predicted_class = 'Glioma'
    elif predicted_class == 1:
        predicted_class = 'Meningioma'
    elif predicted_class == 2:
        predicted_class = 'No Tumor'
    else:
        predicted_class = 'Pituitary Tumor'
    return f'Predicted class: {predicted_class}'