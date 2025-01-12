from typing import Annotated

from msgspec import Meta, Struct


class Person(Struct):
    """Class representing a person.

    Parameters
    ----------
    name : str
        Name of the person.
    """

    name: str
    age: Annotated[int, Meta(description="Age in years (description in the field)")] = 0
