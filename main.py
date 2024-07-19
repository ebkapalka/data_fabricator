from generate_data import create_dataframe
from utilities import timestamp

import pandas as pd
import os


def export_data(data: pd.DataFrame, schema: str, folder: str):
    """
    Export the data to a csv file
    :param data: dataframe to export
    :param schema: name of the schema used to generate the data
    :param folder: folder to save the csv file
    :return: None
    """
    filename = f"{timestamp()}_{schema}_data.csv"
    if not os.path.exists(folder):
        os.makedirs(folder)
    path = os.path.join(folder, filename)
    data.to_csv(path, index=False)


if __name__ == '__main__':
    num_rows = 1000
    schema_name = 'default'
    destination = 'output'
    df = create_dataframe(schema_name, num_rows)

    # export the data to a csv file
    export_data(df, schema_name, destination)
    print(f"Generated {num_rows} rows of data")
    print(f"using schema '{schema_name}' and")
    print(f"saved to '{schema_name}_data.csv'")
