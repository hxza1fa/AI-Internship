from predict import price_predictor
from fastapi import FastAPI 
from diamond_validation import Diamond

api = FastAPI()

@api.post("/predict")
def predict_diamond_price(diamond: Diamond):
    return {
        "price": price_predictor(diamond)
    }