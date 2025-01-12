import pandas as pd
import os

def load_data(file_path):
    """
    Load data from the uploaded file (CSV/Excel).
    """
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path)
    elif file_path.endswith(".xlsx"):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format! Please upload a CSV or Excel file.")

def rename_files_with_mapping(folder_path, naming_format, data):
    """
    Rename files in the folder based on the naming format and data mapping.
    """
    files = os.listdir(folder_path)

    for i, file in enumerate(files):
        if os.path.isfile(os.path.join(folder_path, file)):
            # Extract row data for the current file
            row_data = data.iloc[i]

            # Replace placeholders in the naming format
            new_name = naming_format
            for col in data.columns:
                placeholder = f"{col}"  # e.g., "a1", "a2"
                new_name = new_name.replace(placeholder, str(row_data[col]))

            # Append file extension
            ext = os.path.splitext(file)[-1]
            new_name += ext

            # Rename the file
            old_path = os.path.join(folder_path, file)
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {file} -> {new_name}")
