from faker import Faker
import random

fake = Faker()

schema = {
    'first_name': fake.first_name,
    'last_name': fake.last_name,
    'email': fake.email,
    'phone_number': fake.phone_number,
    'is_active': lambda: random.choice([True, False]),
    'age': lambda: random.randint(18, 70),
    # Add more columns as needed
}
