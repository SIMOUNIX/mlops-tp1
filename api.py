from fastapi import FastAPI
from pydantic import BaseModel
import models_utils

app = FastAPI()

class HouseDetails(BaseModel):
    size: int
    nb_rooms: int
    garden: int

@app.get("/")
def read_root():
    return {"test": "you are now using the API to call the linear regression model on the housing prices dataset"}

@app.post("/predict")
def predict(data: HouseDetails):
    prediction = models_utils.model_predict(data.size, data.nb_rooms, data.garden)
    return {"prediction": prediction}