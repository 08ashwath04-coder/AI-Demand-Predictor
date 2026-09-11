import os
import joblib
import pandas as pd


# Find project root
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../")
)

MODEL_FILE = os.path.join(
    PROJECT_ROOT,
    "ml",
    "models",
    "demand_model.pkl"
)


# Load trained model
model = joblib.load(MODEL_FILE)


def predict_demand(
    product: str,
    price: float,
    discount: float,
    holiday: int,
    month: int,
    day_of_week: int,
    has_festival: int,
    season_encoded: int
):

    # Start with all product columns as 0
    data = {
        "price": price,
        "discount": discount,
        "holiday": holiday,
        "month": month,
        "day_of_week": day_of_week,
        "has_festival": has_festival,
        "season_encoded": season_encoded,

        "product_Biscuit": 0,
        "product_Flag": 0,
        "product_Juice": 0,
        "product_Mango": 0,
        "product_Rice": 0,
        "product_Sweets": 0
    }

    # Activate selected product
    product_column = f"product_{product}"

    if product_column not in data:
        raise ValueError(f"Unsupported product: {product}")

    data[product_column] = 1

    # Convert to DataFrame
    input_data = pd.DataFrame([data])

    # Predict
    prediction = model.predict(input_data)[0]

    return round(float(prediction), 2)