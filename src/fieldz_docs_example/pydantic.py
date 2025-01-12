from pydantic import BaseModel, Field


class MyModel(BaseModel):
    """Pydantic model with field descriptions.

    Parameters
    ----------
    a: int
        Description of a in the docstring
    """

    a: int
    b: float = Field(
        42.0,
        json_schema_extra={"description": "Description of `b` in the field metadata"},
    )
    c: str = Field(default_factory=lambda data: str(data["a"] + data["b"]))
