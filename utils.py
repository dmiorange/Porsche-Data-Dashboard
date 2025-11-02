import pandas as pd
import numpy as np
import os


def load_data():
    file_path = os.path.join("data", "porsche_models.csv")
    df = pd.read_csv(file_path)
    print("✅ Data loaded successfully!")
    print(df.head())
    return df


def clean_data(df):
    print("🔍 Checking for missing values:")
    print(df.isnull().sum())

    # Clean data
    df = df.dropna(subset=['MSRP_USD'])
    df['Battery_kWh'] = df['Battery_kWh'].fillna(0)
    df['Range_mi'] = df['Range_mi'].fillna(0)
    df = df.drop_duplicates()

    print("✅ Data cleaned successfully!")
    print(df.head())

    return df


def save_clean_data(df):
    # Save the cleaned data to a new CSV file
    df.to_csv("data/cleaned_porsche_models.csv", index=False)
    print("✅ Cleaned data saved successfully as cleaned_porsche_models.csv!")