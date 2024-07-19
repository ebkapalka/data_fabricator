from faker import Faker
import random

fake = Faker()

schema = {
    'first_name': fake.first_name,
    'last_name': fake.last_name,
    'age': lambda: random.randint(18, 70),
    # Add more columns as needed
}
