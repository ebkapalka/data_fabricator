import pandas as pd
from collections import defaultdict
import importlib.util
import os
import random


class DataGenerator:
    def __init__(self, schema):
        self.schema = schema

    def generate_row(self):
        row = {}
        for column, generator in self.schema.items():
            if isinstance(generator, list):
                row[column] = random.choice(generator)
            else:
                row[column] = generator()
        return row

    def generate_data(self, num_rows):
        data = [self.generate_row() for _ in range(num_rows)]
        return data


def load_schema(schema_name, basepath='schemas'):
    schema_path = os.path.join(basepath, f'schema_{schema_name}.py')
    spec = importlib.util.spec_from_file_location(schema_name, schema_path)
    schema_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(schema_module)
    return schema_module.schema


def create_dataframe(schema_name, num_rows):
    schema = load_schema(schema_name)
    generator = DataGenerator(schema)
    data = generator.generate_data(num_rows)
    df = pd.DataFrame(data)
    return df
