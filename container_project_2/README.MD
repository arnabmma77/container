# Containerized Python Application

This project is a containerized Python application that processes a sample dataset. It is structured to run in a Docker environment and includes all necessary configurations for setup and execution.

---

## 🛠 Tech Stack
- Python 3.10
- Streamlit
- Scikit-learn
- Pandas
- SHAP
- Docker

---

## 📂 Project Structure

```
evcharge_app/
|
|├— app.py                # Main streamlit app
|├— Dockerfile             # Docker build instructions
|├— requirements.txt       # Python dependencies
|└— data/                  # Sample datasets (CSV)
   └— pages/                 # Streamlit multi-page structure
       ├— 1_📄_Intro.py
       ├— 2_📂_Load_Data.py
       ├— 3_⚙️_Model_Training.py
       └— 4_📊_Visualization_SHAP.py
```

---

## 🚀 How to Run

### 1. Clone or Download the Project
```bash
git clone <repository_link>
cd evcharge_app
```

Or simply download and extract the folder.

---

### 2. Build the Docker Image
```bash
docker build -t evcharge-app .
```

---

### 3. Run the Docker Container
```bash
docker run -p 8501:8501 evcharge-app
```

---

### 4. Open the App

Go to your browser and open:

> http://localhost:8501

✅ Now you can upload a dataset, train models, and view SHAP visualizations!

---

## Application Overview

- The main logic resides in `app.py`, which utilizes the `sample_data.csv` file.
- All Python dependencies are listed in `requirements.txt` and will be installed during Docker image build.
- This setup is ideal for deployment in isolated environments using Docker.

You can also upload your own datasets via the app interface.

---

## 📸 Screenshots

![Screenshot](C:\Users\ARNAB MUKHERJEE\OneDrive\Pictures\Screenshots\Screenshot (248).png)

---

## ✨ Made By

> **Arnab Mukherjee** ❤️

---

## 📜 License
This project is licensed for educational and demonstration purposes.

