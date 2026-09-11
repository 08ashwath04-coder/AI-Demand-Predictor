import pandas as pd

INPUT_FILE = "ml/data/sample/retail_sales.csv"
OUTPUT_FILE = "ml/data/processed/processed_sales.csv"


def preprocess_data():

    # 1. Load original dataset
    df = pd.read_csv(INPUT_FILE)

    # 2. Convert date
    df["date"] = pd.to_datetime(df["date"])

    # 3. Replace missing festival values
    df["festival"] = df["festival"].fillna("None")

    # 4. Create date features
    df["day"] = df["date"].dt.day
    df["month"] = df["date"].dt.month
    df["day_of_week"] = df["date"].dt.dayofweek

    # 5. Festival feature
    df["has_festival"] = (df["festival"] != "None").astype(int)

    # 6. Encode season
    season_mapping = {
        "Winter": 0,
        "Summer": 1,
        "Monsoon": 2
    }

    df["season_encoded"] = df["season"].map(season_mapping)

    # 7. Save processed dataset
    df.to_csv(OUTPUT_FILE, index=False)

    print("✅ Data preprocessing completed!")
    print(f"📊 Rows: {len(df)}")
    print(f"📊 Columns: {len(df.columns)}")
    print(f"📁 Saved to: {OUTPUT_FILE}")

    print("\nMissing values:")
    print(df.isnull().sum())


if __name__ == "__main__":
    preprocess_data()