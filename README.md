# 🚦 Traffic Volume Prediction App

This is a machine learning-based web application built with Flask that predicts urban traffic volume based on various inputs like weather conditions, time features, and more.

## 🧠 Project Overview

This application uses a pre-trained machine learning model to predict traffic volume. The model is trained on traffic and weather data and considers the following features:

* Temperature
* Rain
* Snow
* Cloud coverage
* Weather condition
* Year, Month, Day
* Hour, Minute, Seconds

The web app takes user input, preprocesses the data (using saved encoder/scaler if applicable), and returns the predicted traffic volume.

## 🚀 Tech Stack

* Python 3.8+
* Flask
* Scikit-learn
* Pandas, NumPy
* HTML + CSS (for frontend)
* Pickle (for model and encoder persistence)

## 📁 Project Structure
# 📁 Project Structure


traffic_volume_estimation/
├── Templates/
│   ├── index.html
│   ├── result.html
│   └── traffic int.html
├── static/
│   └── images/
│       └── car.jpg
├── app.py
├── build_encoder.py
├── encoder.pkl
├── model.pkl
├── README.md
├── requirements.txt
└── traffic volume.csv

## ⚙ Setup Instructions

1.  *Clone the repository:*
    bash
    git clone :https://github.com/jayanth11189121/traffic_volume_estimation.git
    cd traffic_volume_estimation
    

2.  *Install Dependencies:*
    Make sure you have pip installed. Then, from the traffic_volume_estimation directory, run:
    bash
    pip install -r requirements.txt
    

## 🚀 How to Run This Project

### 1. Train the Model and Generate Required Files (If not already present)

If encoder.pkl and model.pkl are not present or you wish to retrain:

* *Ensure you have a script for training (e.g., a Jupyter Notebook or a Python script).* Based on your file list, build_encoder.py might be part of this process, or you might have a separate training script/notebook.
* The training process should generate encoder.pkl and model.pkl files in the root of your project directory.

*(Note: If you have a specific notebook or script that generates these, replace the placeholder text below with instructions on how to run it. For example, "Run the train_model.ipynb Jupyter Notebook.")*

### 2. Run the Flask Web Application

After ensuring encoder.pkl and model.pkl are in your traffic_volume_estimation directory, run the Flask app from the project's root:

```bash
python app.py