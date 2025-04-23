 🐳 Streamlit APP with Docker

## 🚀 Prerequisites

Before setting up the environment, ensure you have the following installed on your machine:

- **Docker** 🐳 (Ensure the Docker daemon is running)
- **Python 3.9+** 🐍 (Verify installation with `python --version`)
- **pip** (Ensure it's installed and up to date with `pip --version`)
- **Basic knowledge of Streamlit** 📊

---

## 📂 Directory Structure

```
streamlit_app/
│── .streamlit/
│   └── config.toml
│── src/
│   └── app.py
│── Dockerfile
│── requirements.txt
│── README.md
```

---

## 📜 File Explanations

### 1️⃣ `.streamlit/config.toml`
This file configures Streamlit settings for local development.

```toml
[server]
headless = true
runOnSave = true
fileWatcherType = "poll"
```

### 2️⃣ `src/app.py`
This file contains the core logic of the Streamlit application. It includes:

- **A home page** 🏠 that provides an introduction to the app.
- **A data explorer** 📊 allowing users to upload and inspect CSV files.
- **A visualization page** 📈 that generates interactive charts and graphs.

### 3️⃣ `Dockerfile`
Defines the containerized environment.

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8501
CMD ["streamlit", "run", "src/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### 4️⃣ `requirements.txt`
Contains necessary dependencies:

```
streamlit
pandas
numpy
matplotlib
plotly
```

---

## ⚡ Steps to Run the Project

### 1️⃣ Navigate to the project directory:
```sh
cd path/to/streamlit_app
```

### 2️⃣ Build the Docker image:
```sh
docker build -t streamlit-app .
```

### 3️⃣ Run the container:
```sh
docker run -p 8501:8501 streamlit-app
```

### 4️⃣ Open in Browser:
Go to 👉 **http://localhost:8501** 🌐

---
![image](https://github.com/user-attachments/assets/90d0d185-742c-43ff-ad06-88228f38e9aa)

![image](https://github.com/user-attachments/assets/ccf81653-9f10-4e83-813b-dde1c9d513d4)

## 🎯 Conclusion
You now have a fully functional Streamlit environment running inside Docker! 🚀


