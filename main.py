from utilities.utils_export import export_data
from generate_data import create_dataframe


if __name__ == '__main__':
    num_rows = 1000
    schema_folder = 'schemas'
    # TODO: use the schemas folder
    schema_name = 'default'
    folder_path = 'output'
    df = create_dataframe(schema_name, num_rows)

    # export the data to a csv file
    filename = export_data(
        data=df,
        schema=schema_name,
        folder=folder_path,
        file_type='csv',
        encoding='utf-8',
        header=True,
        line_ending='\n')
    print(f"Generated {num_rows} rows of data")
    print(f"using schema '{schema_name}' and")
    print(f"saved to '{filename}'")
