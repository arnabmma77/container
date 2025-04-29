# EVChargeAI - Smart EV Energy Prediction

Welcome to **EVChargeAI** — a smart Streamlit web application for energy prediction and model explanation for electric vehicles.  
This project helps users:
- Load and explore EV datasets 📂
- Train Machine Learning models ⚙️
- Visualize important features using SHAP 📊
- Explain model decisions in a clear way

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

## 📂 Sample Data

A small EV dataset is provided in the `data/` folder for quick testing:
- `sample_ev_data.csv`

You can also upload your own datasets via the app interface.

---

## 📸 Screenshots
> (Add screenshots here if needed later!)

---

## ✨ Made By

> **Arnab Mukherjee** ❤️

---

## 📜 License
This project is licensed for educational and demonstration purposes.

