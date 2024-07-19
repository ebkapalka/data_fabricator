from generate_data import create_dataframe

if __name__ == '__main__':
    num_rows = 1000
    schema_name = 'default'  # Change to the schema you want to use
    df = create_dataframe(schema_name, num_rows)
    df.to_csv(f'{schema_name}_data.csv', index=False)
    print(f"Generated {num_rows} rows of data "
          f"using schema '{schema_name}' and "
          f"saved to '{schema_name}_data.csv'")
