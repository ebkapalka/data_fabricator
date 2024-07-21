from typing import Callable, Union
import numpy as np
import random

"""
This module contains a selection of utility 
functions for generating biased random data.
"""


def biased_int(val1: int, val2: int, scale: float = 5.0) -> int:
    """
    Generate a random int with a bias towards the lower or higher value
        depending on the order provided.

    :param val1: first value
    :param val2: second value
    :param scale: decay scale for the exponential distribution;
        lower values bias towards the first number, higher values
        flatten the distribution (reduce bias) resulting in a
        more uniform distribution
    :return: biased int that is always between val1 and val2
    """
    if val1 == val2:
        return val1
    min_val = min(val1, val2)
    max_val = max(val1, val2)

    if val1 < val2:
        # Bias towards lower numbers
        val = int(np.random.exponential(scale) + min_val)
        return min(val, max_val)
    else:
        # Bias towards higher numbers
        val = max_val - int(np.random.exponential(scale))
        return max(val, min_val)


def biased_func(func: Callable[[], any],
                default_val: Union[Callable[[], any], any] = None,
                bias_prob: float = 0.1) -> any:
    """
    Provide the output of the func with a probability of bias towards the default_val. For
    example, if the bias_prob is 0.1, there is a 10% chance that the default_val will be
    returned. default_value can be a fixed value or a function that generates a value.

    :param func: function to generate the value
    :param default_val: function or fixed value to bias towards
    :param bias_prob: probability of bias towards the default value;
        higher values bias more towards default_val
    :return: a value from either default_val or the result of func,
        depending on bias_prob
    """
    if random.random() < bias_prob:
        if callable(default_val):
            return default_val()
        return default_val
    return func()
