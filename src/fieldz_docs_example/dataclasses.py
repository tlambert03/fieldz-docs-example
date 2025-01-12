from dataclasses import dataclass, field


@dataclass
class Person:
    """Class representing a person.

    Parameters
    ----------
    name : str
        Name of the person.
    """

    name: str
    age: int = field(
        default=0,
        metadata={"description": "Age in years (description in the field)"},
    )
