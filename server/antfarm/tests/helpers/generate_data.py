"""
Helpers for generating stub data
"""
import random
import string


def generate_random_string():
    """
    Helper to generate a random string
    """
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
