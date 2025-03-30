# Brain Tumor Detection Model

## 📌 Overview
This project is a deep learning-based brain tumor detection model that classifies MRI scan images into different categories. The model leverages convolutional neural networks (CNNs) using architectures such as DenseNet and ResNet.

## 🏗 Project Structure
```
DSAI-Brain-Tumor-Detection/
│── imagesForTesting/  # Folder containing MRI images for testing
│── myenv/              # Virtual environment
│── results/          # Folder containing result images
│── .gitignore         # Git ignore file
│── DenseNet.ipynb     # Model training using DenseNet
│── main.py           # Main script for running predictions
│── my_model.h5         # Saved trained model
│── predictions.ipynb    # Notebook for making predictions
│── README.md         # Project documentation
│── Resnet.ipynb      # Model training using ResNet
```

## 🔧 Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/brain-tumor-detection.git
   cd brain-tumor-detection
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv myenv
   source myenv/bin/activate  # On Windows use: myenv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## 🚀 Usage
### 1️⃣ Train the Model
Run the Jupyter notebooks `DenseNet.ipynb` or `Resnet.ipynb` to train the model.

### 2️⃣ Make Predictions
Use `predictions.ipynb` to load the trained model and predict tumor presence in MRI images.

### 3️⃣ Run the Model Script
Alternatively, run the Python script:
```sh
python main.py --image path/to/image.jpg
```

## 🏆 Results
The model was trained on a dataset with 4 classes and achieved the following results:

- **Final Training Accuracy:** 93.75%
- **Final Training Loss:** 0.1769
- **Final Validation Accuracy:** 81.07%
- **Final Validation Loss:** 0.6776

These results indicate that the model performs well in detecting brain tumors from MRI images. Further improvements can be made by hyperparameter tuning and dataset augmentation.

### 📊 Performance Visualizations
#### 1️⃣ Confusion Matrix
<p align="center">
  <img src="results/Confusion%20Matrix.png" alt="Confusion Matrix"/>
</p>

#### 2️⃣ Accuracy and Loss Graphs
<p align="center">
  <img src="results/epoch%20vs%20accuracy.png" alt="Epoch vs Accuracy"/>
</p>

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).

## 🤝 Contributing
Feel free to submit issues or pull requests if you'd like to improve the model.

## 📬 Contact
For any inquiries, reach out to [anipradhan@gmail.com](mailto:anipradhan.04@gmail.com).

---
### 🚀 Happy Coding!
