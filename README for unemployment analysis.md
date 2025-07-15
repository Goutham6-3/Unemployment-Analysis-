
# Unemployment Data Cleaning Script

This Python script is designed to **load, clean, and prepare unemployment data** from an Excel-exported CSV file titled `Unemployment in India.xlsx.csv`. It performs basic data cleaning operations to ensure the dataset is ready for analysis or visualization.

---

## 📁 Input File

- **Filename**: `Unemployment in India.xlsx.csv`
- **Format**: CSV (Make sure it’s saved correctly from Excel)

> ⚠️ Ensure the file is in the same directory as the script or update the file path in the code accordingly.

---

## ✅ Features of This Script

1. **Imports Required Libraries**
   - Uses `pandas` for data manipulation.

2. **Loads the Dataset**
   - Reads a CSV file containing unemployment data.

3. **Initial Data Inspection**
   - Prints the first 5 rows.
   - Shows column info and summary statistics.

4. **Cleans the Dataset**
   - Strips spaces and converts column names to lowercase.
   - Drops duplicate rows.
   - Converts the `date` column to datetime format.
   - Removes rows with missing `unemployment_rate`.

5. **Final Output**
   - Saves the cleaned data as `cleaned_unemployment_data.csv`.

---

## 🧪 How to Run

1. Make sure you have **Python 3.x** installed.
2. Install the required package (if not already installed):

   ```bash
   pip install pandas

A brief description of what this project does and who it's for

