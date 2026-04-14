# 🧠 AI-Powered Medical Image Analysis System

## 📌 Overview

This project is an end-to-end AI system that analyzes medical images such as X-rays to detect diseases like pneumonia using deep learning techniques.

It includes model training, prediction pipeline, and a web-based interface for real-time interaction.

---

## 🚀 Features

* Deep learning-based image classification
* Medical image analysis (X-ray simulation)
* Streamlit interactive UI
* End-to-end ML pipeline (training → prediction → deployment)
* Real-time image upload and prediction

---

## 🛠 Tech Stack

* Python
* TensorFlow / Keras
* OpenCV
* NumPy
* Streamlit

---

## 📂 Project Structure

```
AI-Medical-Image-Analysis/
│
├── src/                # ML pipeline
├── ui/                 # Streamlit app
├── models/             # Saved models (ignored)
├── data/               # Dataset (ignored)
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

---

## 🧪 Run Training

```bash
python -m src.train
```

---

## 🌐 Run Application

```bash
streamlit run ui/app.py
```

---

## 📸 Usage
<img width="740" height="668" alt="Screenshot (23)" src="https://github.com/user-attachments/assets/a5757f45-7b8b-46de-9d69-e52097819717" />

1. Upload an image (X-ray or any image)
<img width="1920" height="1080" alt="Screenshot (24)" src="https://github.com/user-attachments/assets/904a5dcd-e384-4182-ac64-12686eae5d1d" />

2. The model analyzes the image
<img width="1920" height="1080" alt="Screenshot (25)" src="https://github.com/user-attachments/assets/a41970dc-2d97-44fa-ba75-f54f7b31c586" />

3. Displays prediction (Normal / Pneumonia)

---

## ⚠️ Note

This project uses a simulated dataset for demonstration purposes. For real-world applications, training on clinical datasets is required.

---

## 📈 Future Improvements

* Grad-CAM visualization (heatmaps)
* Real medical dataset integration
* Model optimization
* Cloud deployment (AWS / Docker)

---

## 🎯 Outcome

This project demonstrates the practical application of AI in healthcare, focusing on computer vision and deep learning for medical diagnostics.

---

## 👨‍💻 Author

Challa Kishore 
