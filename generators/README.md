# <div align="center">Seed Data</div>

## Introduction

This module contains functions and seed data for custom random data generators. Data from the `seed_data` folder is loaded into a dictionary of dataframes in `gen_utils.py` upon initialization of the module, which is then utilized by the functions contained within.  The data in seed_data is actual (albeit public non-confidential) data pulled from an Ellucian Banner database; because this application was developed to practice importing student data into a university database, some data (like school CEEB codes) has to actually correspond to real data in order to be useful / importable.

## Usage
### Loading Seed Data:
When the module is initialized, it automatically loads data from the seed_data folder into a global dictionary of dataframes.

### Generating Random Data:
Here are some examples of how to use the functions provided by this module:

 ```python
from generators import (
    random_school, 
    random_school_name, 
    random_school_ceeb
)

# Generate a random school tuple (school_name, school_ceeb)
print(random_school())

# Generate a random school name
print(random_school_name())

# Generate a random school CEEB code
print(random_school_ceeb())
```

## Expanding Functionality:

1. **Add a new data file** to the `seed_data` folder. The file must be a CSV with a header.
2. **[Optional] Add a new `*.py` file** to the parent module that uses the new data file. See existing `gen_*` files for examples.
3. **Update `__init__.py`**:
    - Add the new data file to the `csv_files` dictionary.
    - Add any newly created functions to the `__all__` list.
