from typing import Callable, Union
import importlib.util
import pandas as pd
import random
import os

# Define type aliases
GeneratorFunction = Callable[[], Union[str, int, float, bool]]
GeneratorList = list[Union[str, int, float, bool]]
SchemaValue = Union[GeneratorFunction, GeneratorList]
SchemaType = dict[str, SchemaValue]


class DataGenerator:
    """
    A class to generate data based on a schema
    """
    def __init__(self, schema: SchemaType):
        self.schema = schema

    def generate_row(self) -> dict:
        """
        Generate a single row of data based on the schema
        :return: dict with column names as keys and generated values as values
        """
        row = {}
        for column, generator in self.schema.items():
            if isinstance(generator, list):
                row[column] = random.choice(generator)
            else:
                row[column] = generator()
        return row

    def generate_data(self, num_rows: int) -> list[dict]:
        """
        Generate multiple rows of data based on the schema
        :param num_rows: number of rows to generate
        :return: list of dicts where each dict represents a row of data
        """
        data = [self.generate_row() for _ in range(num_rows)]
        return data


def load_schema(schema_name: str, base_path="schemas") -> SchemaType:
    """
    Load a schema from a file
    :param schema_name: schema name
    :param base_path: folder where schema files reside
    :return: SchemaType object
    """
    schema_path = os.path.join(base_path, f'schema_{schema_name}.py')
    spec = importlib.util.spec_from_file_location(schema_name, schema_path)
    schema_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(schema_module)
    return schema_module.schema


def create_dataframe(schema_name: str, num_rows: int, schema: SchemaType = None) -> pd.DataFrame:
    """
    Create a pandas DataFrame with generated data based on a schema
    :param schema_name: name of the schema to use without prefix or extension
    :param num_rows: number of rows to generate
    :param schema: optional schema dictionary
    :return: dataframe with generated data
    """
    if not schema:
        schema = load_schema(schema_name)
    generator = DataGenerator(schema)
    data = generator.generate_data(num_rows)
    df = pd.DataFrame(data)
    return df
