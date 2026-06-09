<h1 align="center"> ♨︎ CircuitGuide ♨︎ </h1>
<h3 align="center">AI-Based PCB Defect Detection System</h3>

<p align="center">
  <b>Detect • Analyze • Improve PCB Quality using AI</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
  <img src="https://img.shields.io/badge/YOLOv8m-FF6F00?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Computer%20Vision-000000?style=for-the-badge"/>
</p>

---

## 🧠 About CircuitGuide

CircuitGuide is an **AI-powered PCB defect detection system** that automatically identifies defects in Printed Circuit Boards using **Deep Learning and Computer Vision**.

The goal of this project is to reduce manual inspection effort and improve accuracy in industrial PCB quality control.

---

## 🎯 Problem Statement

Manual PCB inspection:
- ⏱️ Takes a lot of time  
- ❌ Is prone to human error  
- 💸 Increases manufacturing cost  

CircuitGuide solves this problem by using an AI model to detect defects automatically from PCB images.

---

## 🚀 Features

- 🔍 Automatic detection of PCB defects  
- 🧠 YOLO-based deep learning model  
- ⚡ FastAPI backend for inference  
- 📸 Image upload and annotated output  
- 📊 Defect count summary  
- 📍 Defect location table  
- ⬇️ Download annotated images and reports  

---

## 🛠️ Tech Stack

**Programming Language**  
- Python  

**AI / Machine Learning**  
- YOLOv8  
- OpenCV  
- NumPy  
- Pandas  

**Backend**  
- FastAPI  
- Uvicorn  

---

## 🧩 System Architecture
PCB Image Upload
     ↓
FastAPI Backend
     ↓
YOLO Defect Detection Model
     ↓
Annotated Image + Defect Data
     ↓
Download Results


---

## 📸 Screenshots

### 🔹 Input PCB Image
![Input PCB](Output-Images/1.png)

### 🔹 Defect Detection Output
![Detection Output](Output-Images/2.png)

### 🔹 Annotated PCB with Bounding Boxes
![Annotated PCB](Output-Images/6.png)

### 🔹 Defect Count & Location Table
![Defect Table](Output-Images/7.png)

### 🔹 Streamlit / UI View
![UI View](Output-Images/8.png)

---

## ⚙️ How to Run the Project

Clone the repository  
`git clone https://github.com/prashantyadav12/CircuitGuide-PCB_Defect_Detection.git`

Move into project folder  
`cd CircuitGuide-PCB_Defect_Detection`

Create virtual environment  
`python -m venv venv`

Activate virtual environment (Windows)  
`venv\Scripts\activate`

Activate virtual environment (Mac/Linux)  
`source venv/bin/activate`

Install dependencies  
`pip install -r requirements.txt`

Run FastAPI server  
`uvicorn main:app --reload`

Open Swagger Docs  
`http://127.0.0.1:8000/docs`

---

## 🌐 API Endpoints

- `GET /` → Health check  
- `POST /detect` → Upload PCB image for defect detection  

---

## 📊 Project Outcome

- ✔ Accurate multi-defect detection  
- ✔ Fast inference speed  
- ✔ Clear visual results  
- ✔ Industry-oriented workflow  

---

## 🔮 Future Enhancements

- Web frontend dashboard  
- Cloud deployment  
- Live camera inspection  
- Defect severity analysis  
- Analytics and reporting  

---

## 👨‍💻 Author

**Prashant Yadav**  
Computer Science (AI) Student  
AI • Backend • System Integration  

🔗 LinkedIn:  
https://www.linkedin.com/in/prashant-yadav-638684298/

---

<p align="center">
  <img src="https://visitcount.itsvg.in/api?id=circuitguide&label=Project%20Views&color=0&pretty=true"/>
</p>
