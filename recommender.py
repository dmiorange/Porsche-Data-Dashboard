import pandas as pd
from utils import load_data, clean_data

def load_cleaned_data():
    df = pd.read_csv("data/cleaned_porsche_models.csv")
    print("✅ Cleaned data loaded successfully!")
    print(df.head())
    return df

def get_user_prefrences():
    print("\n🏎️  Welcome to the Porsche Recommender!\n")
    budget = float(input("Enter your Budget (Usd): "))
    min_hp = float(input("Enter your minimum horse power: "))
    max_hp = float(input("Enter your maximum horse power: "))
    body_type = input("Prefered body type (Coupe/Sedan/SUV?): ")
    condition = input("Prefered condition (New/Used?): ")
    drive_layout = input("Prefer (AWD/RWD): ")
    return budget, min_hp, max_hp, body_type, condition, drive_layout

def recommend_porsche(df, budget, min_hp, max_hp, body_type, drive_layout):
    results = df[
        (df["MSRP_USD"] <= budget) &
        (df["Power_hp"] >= min_hp) & 
        (df["Power_hp"] <= max_hp) &
        (df["Body"].str.contains(body_type, case=False)) &
        (df["Drive"] == drive_layout)
    ]

    results = results.sort_values(by="Power_hp", ascending=False)

    return results

def show_results(results):
    if results.empty:
        print("\n❌ No Porsche models match your search.\n")
    else:
        print("\n✅ Top Porsche Recommendations:\n")
        # Select key columns to display
        print(results[["Model", "Body", "Power_hp", "MSRP_USD", "Drive", "ZeroTo60_s"]].head(10))

if __name__ == "__main__":
    import pandas as pd

    df = pd.read_csv("data/cleaned_porsche_models.csv")

    print("\n🏎️ Welcome to the Porsche Recommender!\n")

    # Ask user for input
    budget = float(input("Enter your maximum budget (USD): "))
    min_hp = int(input("Enter your minimum horsepower: "))
    max_hp = int(input("Enter your maximum horsepower: "))
    body_type = input("Preferred body type (Coupe/Sedan/SUV)? ").capitalize()
    drive_layout = input("Drive layout (RWD/AWD)? ").upper()

    # Get recommendations
    results = recommend_porsche(df, budget, min_hp, max_hp, body_type, drive_layout)

    # Display results
    show_results(results)
