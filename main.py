from utilities.utils_export import export_data
from generate_data import create_dataframe, load_schema


if __name__ == '__main__':
    num_rows = 10000
    schema_folder = 'schemas'
    schema_name = 'inquiry_visit'
    folder_path = 'output'
    schema = load_schema(schema_name, schema_folder)
    df = create_dataframe(schema_name, num_rows, schema)

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
