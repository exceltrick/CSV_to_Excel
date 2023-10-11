import pandas as pd
import os

def convert_csv_to_excel(csv_filename, excel_filename):
    try:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(csv_filename)
        
        # Convert the DataFrame to an Excel file
        df.to_excel(excel_filename, index=False)
        
        print(f"CSV file '{csv_filename}' successfully converted to Excel '{excel_filename}'.")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    # Specify the CSV and Excel file names
    csv_file = "input.csv"
    excel_file = "output.xlsx"
    
    # Check if the CSV file exists before attempting conversion
    if os.path.isfile(csv_file):
        convert_csv_to_excel(csv_file, excel_file)
    else:
        print(f"Error: CSV file '{csv_file}' not found.")
