# Email Spam Detector

ML-powered email spam detection with React frontend (98.79% accuracy)

## Quick Start

### 1. Backend Setup
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### 2. Frontend Setup (New Terminal)
```bash
cd frontend
npm install
npm start
```

App opens at http://localhost:3000

## Tech Stack
- **Backend:** Python, Flask, Scikit-learn, NLTK
- **Frontend:** React, Framer Motion
- **ML:** Logistic Regression, TF-IDF (3000 features)

## Model Performance
- Accuracy: 98.79%
- Precision: 94.16%
- Recall: 96.99%
- Dataset: 11,145 emails

## Project Structure
```
email-spam-detector/
├── frontend/          # React app
├── app.py            # Flask API
├── preprocessing.py  # Text preprocessing
├── train_full_model.py  # Model training
├── model.pkl         # Trained model
├── tfidf_vectorizer.pkl  # Vectorizer
└── requirements.txt  # Dependencies
```

## Retrain Model
```bash
python train_full_model.py
```
