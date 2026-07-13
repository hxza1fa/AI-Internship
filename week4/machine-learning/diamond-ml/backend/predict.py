import diamond_validation as dv
import numpy as np
import joblib

model = joblib.load("models/diamond_prediction_model.pkl")
encoder = joblib.load("encoders/diamond_features_ordinal_encoder")

def price_predictor(diamond: dv.Diamond) -> float:
    features = diamond.model_dump()

    X_carat = np.array([diamond.carat])
    X_transformed = encoder.fit_transform([[diamond.cut, diamond.color, diamond.clarity]])
    X_post_cat = np.array([[diamond.depth, diamond.table, diamond.x, diamond.y, diamond.z]])

    X = np.column_stack((X_carat, X_transformed))
    X = np.column_stack((X, X_post_cat))

    y = model.predict(X)[0]

    return round(float(y), 2)