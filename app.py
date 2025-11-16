from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
import joblib

app = FastAPI()

# -------------------------------
# Middleware for CORS (frontend calls)
# -------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # for local testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# Load Model and Scaler
# -------------------------------
model = joblib.load("model.pkl")
scaler = joblib.load("Scaler.pkl")

# -------------------------------
# For rendering index.html
# -------------------------------
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    """Serve the frontend HTML file."""
    return templates.TemplateResponse("index.html", {"request": request})


# -------------------------------
# Pydantic model for input data
# -------------------------------
class LoanData(BaseModel):
    x1: float
    x2: float
    x3: float
    x4: float
    x5: float


# -------------------------------
# Prediction endpoint
# -------------------------------
@app.post("/predict/")
def predict_loan(data: LoanData):
    try:
        # Convert input into numpy array
        input_data = np.array([[data.x1, data.x2, data.x3, data.x4, data.x5]])

        # Scale the input using the same scaler used during training
        scaled_input = scaler.transform(input_data)

        # Predict
        prediction = int(model.predict(scaled_input)[0])

        return {"prediction": prediction}

    except Exception as e:
        return {"error": str(e)}