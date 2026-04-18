# 🌾 Crop AI Assistant – Smart Crop Disease Detection & Advisory System

## 📖 Overview
The **Crop AI Assistant** is a web-based application built using Streamlit that helps users detect crop diseases from leaf images and provides treatment recommendations.

It combines **Machine Learning (PyTorch)** with a simple UI to deliver accurate predictions along with symptoms, treatment guidance, and preventive measures.

The system also includes a **chatbot assistant** for interactive support.

---

## 🚀 Features

- 🌾 **Crop Disease Detection**  
  Upload a leaf image and predict the disease using ML models.

- 🎯 **Prediction Confidence**  
  Displays how accurate the prediction is.

- 📄 **Automated PDF Report**  
  Generates a downloadable report including:
  - Detected disease  
  - Symptoms  
  - Treatment guidance  
  - Preventive measures  

- 🤖 **Chatbot Assistance**  
  Interactive chatbot for crop-related queries.

- 🔐 **User Authentication**  
  Login and registration system.

- 📊 **Multiple Model Support**  
  Select different models for prediction.

---

## 🛠️ Tech Stack

- **Frontend & Backend:** Streamlit  
- **Machine Learning:** PyTorch  
- **Image Processing:** PIL  
- **PDF Generation:** ReportLab  
- **Database:** SQLite  
- **Language:** Python  

---

## 🧠 How It Works

1. User logs into the system  
2. Uploads a crop leaf image  
3. Selects a prediction model  
4. System processes the image using ML model  
5. Displays:
   - Disease name  
   - Confidence score  
   - Treatment & prevention details  
6. User downloads PDF report  
7. Chatbot provides assistance  

---

## ▶️ How to Run

```bash
git clone <your-repo-link>
cd crop_pulse_disease_project

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt

streamlit run app.py




