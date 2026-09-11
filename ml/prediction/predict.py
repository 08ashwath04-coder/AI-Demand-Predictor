import joblib
import pandas as pd


# --------------------------------------------------
# 1. Load trained model
# --------------------------------------------------

MODEL_FILE = "ml/models/demand_model.pkl"

model = joblib.load(MODEL_FILE)

print("🤖 Trained demand model loaded successfully!")


# --------------------------------------------------
# 2. Create a NEW situation
# --------------------------------------------------

new_data = pd.DataFrame([
    {
        "price": 30,
        "discount": 10,
        "holiday": 1,
        "month": 8,
        "day_of_week": 5,
        "has_festival": 1,
        "season_encoded": 2,

        "product_Biscuit": 0,
        "product_Flag": 1,
        "product_Juice": 0,
        "product_Mango": 0,
        "product_Rice": 0,
        "product_Sweets": 0
    }
])


# --------------------------------------------------
# 3. Predict demand
# --------------------------------------------------

prediction = model.predict(new_data)

predicted_demand = prediction[0]


# --------------------------------------------------
# 4. Display result
# --------------------------------------------------

print("\n📦 DEMAND PREDICTION")
print("---------------------------")
print("Product: Flag")
print("Date: August 15")
print("Festival: Independence Day")
print("Price: ₹30")
print("Discount: 10%")

print(f"\n🤖 Predicted demand: {predicted_demand:.0f} units")