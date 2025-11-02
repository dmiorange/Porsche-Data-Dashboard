# Porsche Data Dashboard

A small interactive CLI to explore and recommend Porsche models from the provided dataset.

The script loads raw model data, performs basic cleaning, saves a cleaned CSV, and lets you query for recommended models by budget, horsepower, body type, and drive layout.

## Project layout

- `main.py` - CLI entry point. Loads data, runs cleaning, prompts the user for preferences, and shows recommendations.
- `recommender.py` - Recommendation logic and result display helpers.
- `utils.py` - Data loading, cleaning, and saving utilities.
- `requirements.txt` - Python dependencies (install with pip).
- `data/` - CSV data files:
  - `porsche_models.csv` - Raw dataset
  - `cleaned_porsche_models.csv` - Saved cleaned dataset created by the program
- `notes.txt` - Misc notes

## Prerequisites

- Python 3.8+ installed
- Windows PowerShell (examples below use PowerShell)

## Install

Open PowerShell in the project root (where `main.py` is) and run:

```powershell
python -m pip install --upgrade pip; \
python -m pip install -r requirements.txt
```

If you prefer a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run

From the project root run:

```powershell
python main.py
```

The CLI will:
- Load and clean the data (saving `data/cleaned_porsche_models.csv`).
- Prompt for:
  - Maximum budget (USD)
  - Minimum horsepower
  - Maximum horsepower
  - Preferred body type (Coupe/SUV/Sedan)
  - Drive layout (RWD/AWD)
- Print matching model recommendations.

Example inputs when prompted:
- Budget: `100000`
- Min HP: `300`
- Max HP: `500`
- Body type: `Coupe`
- Drive layout: `AWD`

## Notes

- The program expects the CSV files to be present in the `data/` folder. If you replace or update the raw CSV, re-run `main.py` to regenerate `data/cleaned_porsche_models.csv`.
- If you see encoding or path problems on Windows when reading/writing CSVs, make sure PowerShell is running with the correct working directory (the project root) and that OneDrive syncing isn't locking the files.

## Contributing

Small fixes and improvements welcome. Suggested small PRs:
- Add more robust validation for user input in `main.py`.
- Add unit tests for `recommender.py` logic.

## License

created by DmiOrange
