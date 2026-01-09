# 💸 NovaPay: Real-Time Fraud Detection System

A production-ready machine learning project that detects fraudulent financial transactions in real-time. Built with FastAPI for backend inference, Streamlit for the frontend dashboard, and LightGBM for the predictive model, the system is fully containerized using Docker.

---

## 📌 Project Overview

Fraud in digital payments is a growing concern in the financial world. This project implements a real-time fraud detection pipeline designed for **scalability**, **explainability**, and **ease of use**. 

It simulates a real-world fraud detection architecture where:
- Transactions are received in real-time
- A machine learning model predicts the fraud risk
- A dashboard allows analysts to interact with results and insights

## 🎯 Key Features

- ⚙️ **Machine Learning Model**: LightGBM classifier trained on synthetic transactional data.
- 🚀 **Real-Time Inference API**: Built with FastAPI and served via Uvicorn.
- 📊 **Interactive UI**: Streamlit app with feature inputs, fraud predictions, SHAP explanations, and dashboard insights.
- 🐳 **Dockerized**: Easily build and deploy the backend and frontend with Docker & Docker Compose.

## ⚙️ Tech Stack

| Layer         | Tools Used                              |
|---------------|------------------------------------------|
| ML Model      | LightGBM, Scikit-learn                   |
| API Backend   | FastAPI, Pydantic, Uvicorn               |
| UI Frontend   | Streamlit, SHAP, Plotly, Matplotlib      |
| Deployment    | Docker, Docker Compose                   |
| Dev/IDE       | Python 3.10+, VS Code / Anaconda         |

## 📊 Model & Performance
- Trained on a balanced dataset of synthetic transactions.
- Achieved high recall for fraud detection (critical for fraud use-cases).
- SHAP values included for full model explainability.

## 📂 Project Structure
NovaPay_Fraud/
│
├── app.py # FastAPI backend
├── app_ui.py # Streamlit frontend app
├── best_lgb.pkl # Trained LightGBM model
├── requirements.txt # Python dependencies
├── Dockerfile # Backend Docker config
├── docker-compose.yml # Combined service deployment
├── notebooks/ # Exploratory analysis and model development
└── README.md # Project documentation (you are here)

## 🔍 Dashboard Features
- 💡 Input transaction fields and receive fraud prediction in real-time.
- 📈 Visualize feature importance and SHAP-based decision explanations.
- 📋 Navigation tabs: Home, Dashboard, Performance, Recommendations.

## ✅ Results
- Delivered a working end-to-end fraud detection system.
- Real-time scoring pipeline from frontend to backend.
- Production-ready Dockerized architecture.
- Advanced analytics using SHAP and dashboards.

## 📌 Recommendations
- Periodically retrain model on fresh data.
- Integrate into financial transaction pipelines for live fraud monitoring.
- Expand UI with user authentication and logging.
- Deploy backend with Gunicorn + NGINX in production.
