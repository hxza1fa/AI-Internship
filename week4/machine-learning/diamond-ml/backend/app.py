from predict import price_predictor
from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from diamond_validation import Diamond

api = FastAPI()

# Some issues with CORS

api.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@api.post("/predict")
def predict_diamond_price(diamond: Diamond):
    return {
        "price": price_predictor(diamond)
    }