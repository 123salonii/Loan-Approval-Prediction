# 🏦 Loan Approval Predictor

A machine learning–based web application that predicts whether a loan will be **Approved** or **Rejected** based on user financial details.

---

## 🚀 Features
- Predicts loan approval using ML model  
- Clean and simple Flask web interface  
- Real-time prediction  
- Easy to run locally  
- Trained on loan applicant dataset  

---

## 🖼 Screenshots

### ✔ Loan Approved
<img width="767" height="841" alt="Screenshot 2025-11-14 103625" src="https://github.com/user-attachments/assets/09affddd-da69-48c3-bb76-47c407e07997" />


### ✖ Loan Rejected
<img width="749" height="819" alt="Screenshot 2025-11-14 103656" src="https://github.com/user-attachments/assets/67322210-50ac-45db-9638-0e88fc1dc2d4" />


> Upload your images into an **assets** folder in the repo  
> Example: `assets/loan_approved.png`

---

## 📊 Input Features Used for Prediction

| Feature | Description |
|--------|-------------|
| Married | 0 = No, 1 = Yes |
| Applicant Income | Monthly income |
| Education | 0 = Not Graduate, 1 = Graduate |
| Loan Amount | Requested loan amount |
| Credit History | 1 = Good history, 0 = Poor history |

---

## 🧠 Machine Learning Model Details

- Algorithm: Logistic Regression (or your model)
- Preprocessing: StandardScaler  
- Model Files:  
  - `model.pkl`  
  - `scaler.pkl`

---

## 🛠 Tech Stack

**Backend:** Python, Flask, Scikit-Learn  
**Frontend:** HTML, CSS  
**Libraries:** Pandas, NumPy  

---

## 📁 Project Structure

```
Loan_Prediction/
│── app.py
│── model.pkl
│── scaler.pkl
│── requirements.txt
│── templates/
│     └── index.html
│── static/
│     └── style.css
│── assets/
│     ├── loan_approved.png
│     └── loan_rejected.png
└── README.md
```

---

## ▶️ How to Run

### 1️⃣ Install required libraries
```bash
pip install -r requirements.txt
```

### 2️⃣ Run the application
```bash
python app.py
```

### 3️⃣ Open in browser
```
http://127.0.0.1:5000/
```

---

## 📌 Future Enhancements
- Add more input features  
- Deploy online (Render/Netlify/AWS)  
- Add database support  
- Improve UI  

---

## 🤝 Contributing
Pull requests are welcome!

---

## ⭐ Support
If this project helped you, please star the repo ⭐

