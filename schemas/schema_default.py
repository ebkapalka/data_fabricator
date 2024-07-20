from typing import Callable, Union
from faker import Faker
import random

fake = Faker()

GeneratorFunction = Callable[[], Union[str, int, float, bool]]
GeneratorList = list[Union[str, int, float, bool]]
SchemaValue = Union[GeneratorFunction, GeneratorList]

schema: dict[str, SchemaValue] = {
    'first_name': fake.first_name,
    'last_name': fake.last_name,
    'age': lambda: random.randint(18, 70),
    # Add more columns as needed
}
