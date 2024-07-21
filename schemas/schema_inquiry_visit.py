from typing import Callable, Union
from faker import Faker

from utilities.utils_biased_rands import (
    biased_func, biased_int)

fake = Faker()
GeneratorFunction = Callable[[], Union[str, int, float, bool]]
GeneratorList = list[Union[str, int, float, bool]]
SchemaValue = Union[GeneratorFunction, GeneratorList]

schema: dict[str, SchemaValue] = {
    'first_name': fake.first_name,
    'middle_name': fake.last_name,
    'last_name': fake.last_name,
    'addr1': fake.street_address,
    'addr2': lambda: biased_func(
        fake.secondary_address,
        default_val=None,
        bias_prob=0.05),
    'city': fake.city,
    'state': fake.state_abbr,
    'zip5': fake.zipcode,
    'date_of_birth': fake.date_of_birth,
    'email': fake.email,
    #.....
    'age': lambda: biased_int(17, 55, scale=2.0),
    # Add more columns as needed
}

"""
  first_name	
  middle_name	
  last_name	
  addr1	
  addr2	
  city	
  state	
  zip5	
  date_of_birth	
  email	pr_type	permanent_phone	cl_type	cell_phone	gender	ethnicity	race_1	race_2	race_3	race_4	race_5	race_6	hs_ceeb	grad_date	start_term	college_code	major1	admit_type	parent1_relationship	parent1_first_name	parent1_last_name	parent1_email	parent2_relationship	parent2_first_name	parent2_last_name	parent2_email	undefined	source_method	source_category	contact_type
"""
