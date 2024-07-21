from typing import Dict
import pandas as pd

# Global dictionary to store dataframes
dataframes: Dict[str, pd.DataFrame] = {}


def load_csv_data(file_path: str, key: str) -> None:
    """
    Load CSV data into a global dictionary of dataframes.
    :param file_path: Path to the CSV file
    :param key: Key to store the dataframe in the global dictionary
    """
    global dataframes
    dataframes[key] = pd.read_csv(file_path)


def get_random_row(key: str) -> pd.Series:
    """
    Return a random row from the dataframe stored in the global dictionary.
    :param key: Key to access the dataframe in the global dictionary
    :return: A random row from the dataframe as a Pandas Series
    """
    if key not in dataframes or dataframes[key].empty:
        raise ValueError(f"Data for key '{key}' is not loaded. Please load the CSV file first.")
    return dataframes[key].sample(n=1).iloc[0]
