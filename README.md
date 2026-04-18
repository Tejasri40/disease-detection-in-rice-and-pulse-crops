📌 Project Title

Crop AI Assistant – Smart Crop Disease Detection & Advisory System

📖 Overview

The Crop AI Assistant is an intelligent web-based application developed using Streamlit that helps farmers and users detect crop diseases from leaf images and provides treatment recommendations.

The system integrates Machine Learning (PyTorch models) with a user-friendly interface to deliver accurate disease predictions along with detailed guidance such as symptoms, treatment methods, and preventive measures.

In addition, the application includes a chatbot assistant that allows users to interact and get instant information about crop diseases.

🚀 Features
🌾 Crop Disease Detection
Upload a leaf image and predict the disease using trained ML models.
🎯 Prediction Confidence
Displays how accurate the prediction is.
📄 Automated PDF Report
Generates a downloadable report including:
Detected disease
Symptoms
Treatment guidance
Preventive measures
🤖 Chatbot Assistance
Interactive chatbot to answer queries related to crop diseases.
🔐 User Authentication
Secure login and registration system.
📊 Multiple Model Support
Users can select different trained models for prediction.
🛠️ Tech Stack
Frontend & Backend: Streamlit
Machine Learning: PyTorch
Image Processing: PIL (Python Imaging Library)
PDF Generation: ReportLab
Database: SQLite (for user authentication)
Language: Python
🧠 How It Works
User logs into the system
Uploads a crop leaf image
Selects a prediction model
System processes the image using a trained ML model
Displays:
Disease name
Confidence score
Treatment & prevention details
User can download a PDF report
Chatbot provides additional assistance
📂 Project Structure
crop_pulse_disease_project/
│
├── app.py
├── auth.py
├── src/
│   ├── predict.py
│   ├── model_config.py
│   └── services/
│       ├── auth_service.py
│       └── prediction_service.py
│
├── data/
│   └── disease_info.py
│
├── models/
├── requirements.txt
└── README.md
▶️ How to Run
git clone <your-repo-link>
cd crop_pulse_disease_project

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt

streamlit run app.py
🎯 Use Cases
Farmers for early disease detection
Agriculture students for learning
Researchers for crop analysis
Agri-tech solutions
🌟 Future Enhancements
AI-powered chatbot (ChatGPT integration)
Multi-language support (Telugu, Hindi, etc.)
Mobile app version
Real-time camera detection
Cloud deployment
