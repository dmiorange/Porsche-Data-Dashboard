from utils import load_data, clean_data, save_clean_data
from recommender import recommend_porsche, show_results
import pandas as pd


def main():
    print("===========================================")
    print("🏎️  Welcome to the Porsche Data Dashboard!")
    print("===========================================\n")

    df = load_data()

    df = clean_data(df)

    save_clean_data(df)

    df = pd.read_csv("data/cleaned_porsche_models.csv")

    print("\nLet's find your perfect Porsche! 🔍\n")
    budget = float(input("Enter your maximum budget (USD): "))
    min_hp = int(input("Enter your minimum horsepower: "))
    max_hp = int(input("Enter your maximum horsepower: "))
    body_type = input("Preferred body type (Coupe/SUV/Sedan)? ").capitalize()
    drive_layout = input("Drive layout (RWD/AWD)? ").upper()

    results = recommend_porsche(df, budget, min_hp, max_hp, body_type, drive_layout)

    show_results(results)


if __name__ == "__main__":
    main()