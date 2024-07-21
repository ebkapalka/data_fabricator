from .gen_utils import get_random_row

from typing import Tuple


def random_school() -> Tuple[str, str]:
    """
    Return a random tuple of (school_name, school_ceeb).
    :return: A tuple containing a random school name and CEEB code
    """
    random_row = get_random_row('schools')
    return random_row['school_name'], random_row['school_ceeb']


def random_school_name() -> str:
    """
    Return a random school name.
    :return: A random school name
    """
    return get_random_row('schools')['school_name']


def random_school_ceeb() -> str:
    """
    Return a random school CEEB code.
    :return: A random school CEEB code
    """
    return get_random_row('schools')['school_ceeb']
