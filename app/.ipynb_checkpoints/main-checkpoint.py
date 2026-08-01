from fastapi import FastAPI
from app.schemas import StudentInput
from app.model_loader import model
from app.logger import logger
from app.config import APP_NAME, VERSION

app = FastAPI(
    title=APP_NAME,
    version=VERSION,
    description="Student Marks Prediction API"
)


@app.get("/")
def home():

    return {
        "message":"Welcome to Student Marks Prediction API"
    }


@app.get("/health")
def health():

    return {
        "status":"healthy"
    }


@app.get("/version")
def version():

    return {
        "version":VERSION
    }


@app.post("/predict")
def predict(student: StudentInput):

    prediction = model.predict([[student.hours]])

    logger.info(
        f"Prediction requested for {student.hours} Hours"
    )

    return {

        "Hours":student.hours,

        "Predicted Marks":round(
            prediction[0],
            2
        )

    }
