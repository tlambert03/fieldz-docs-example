from pydantic import BaseModel, Field


class MyModel(BaseModel):
    a: int
    b: float
    c: str = Field(default_factory=lambda data: str(data["a"] + data["b"]))
