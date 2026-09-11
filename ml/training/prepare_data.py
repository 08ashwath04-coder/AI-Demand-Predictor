import pandas as pd
from sklearn.model_selection import train_test_split

# Load processed data
DATA_FILE = "ml/data/processed/processed_sales.csv"

df = pd.read_csv(DATA_FILE)

# Convert product names into numerical columns
df = pd.get_dummies(
    df,
    columns=["product"],
    dtype=int
)

# Features (inputs)
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

# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Total records:", len(df))

print("\nFeatures after encoding:")
print(X.columns.tolist())

print("\nTraining data:")
print("X_train:", X_train.shape)
print("y_train:", y_train.shape)

print("\nTesting data:")
print("X_test:", X_test.shape)
print("y_test:", y_test.shape)

print("\nFirst 5 training rows:")
print(X_train.head())