import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score


# --------------------------------------------------
# 1. Load processed data
# --------------------------------------------------

DATA_FILE = "ml/data/processed/processed_sales.csv"

df = pd.read_csv(DATA_FILE)


# --------------------------------------------------
# 2. Convert product into numerical columns
# --------------------------------------------------

df = pd.get_dummies(
    df,
    columns=["product"],
    dtype=int
)


# --------------------------------------------------
# 3. Select input features
# --------------------------------------------------

feature_columns = [
    "price",
    "discount",
    "holiday",
    "month",
    "day_of_week",
    "has_festival",
    "season_encoded",
    "product_Biscuit",
    "product_Flag",
    "product_Juice",
    "product_Mango",
    "product_Rice",
    "product_Sweets"
]

X = df[feature_columns]

# Target
y = df["quantity_sold"]


# --------------------------------------------------
# 4. Split data
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# --------------------------------------------------
# 5. Create the ML model
# --------------------------------------------------

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)


# --------------------------------------------------
# 6. Train the model
# --------------------------------------------------

print("🤖 Training demand prediction model...")

model.fit(X_train, y_train)

print("✅ Model training completed!")


# --------------------------------------------------
# 7. Make predictions
# --------------------------------------------------

y_pred = model.predict(X_test)


# --------------------------------------------------
# 8. Evaluate the model
# --------------------------------------------------

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n📊 MODEL PERFORMANCE")
print("---------------------------")
print(f"Mean Absolute Error: {mae:.2f}")
print(f"R² Score: {r2:.2f}")


# --------------------------------------------------
# 9. Show actual vs predicted
# --------------------------------------------------

print("\n📈 ACTUAL vs PREDICTED")

for actual, predicted in zip(y_test, y_pred):
    print(
        f"Actual: {actual:>4} | "
        f"Predicted: {predicted:.2f}"
    )


# --------------------------------------------------
# 10. Save the trained model
# --------------------------------------------------

MODEL_FILE = "ml/models/demand_model.pkl"

joblib.dump(model, MODEL_FILE)

print(f"\n💾 Model saved to: {MODEL_FILE}")