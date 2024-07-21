from .gen_schools_hs import random_school, random_school_name, random_school_ceeb
from .gen_utils import load_csv_data
import os

# Define paths to your CSV files and their corresponding keys
csv_files = {
    'schools': 'path_to_your_school_data.csv',
    # Add more CSV files and keys as needed
}

# Load all CSV files into the global dictionary
for key, file_path in csv_files.items():
    if os.path.exists(file_path):
        load_csv_data(file_path, key)
    else:
        print(f"Warning: {file_path} does not exist and will not be loaded.")

# Expose the necessary functions
__all__ = [
    'load_csv_data',
    'random_school',
    'random_school_name',
    'random_school_ceeb'
]
