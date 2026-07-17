from predict import price_predictor
from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from diamond_validation import Diamond

api = FastAPI()

# Some issues with CORS

api.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://gemiq-ml.vercel.app", "https://gemiq-b5kc9il6b-i246078-3606s-projects.vercel.app",],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@api.post("/predict")
def predict_diamond_price(diamond: Diamond):
    print(f"Diamond sent: {diamond}")

    return {
        "price": price_predictor(diamond)
    }