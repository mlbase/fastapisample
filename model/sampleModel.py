from typing import Union
from pydantic import BaseModel


class SampleModel(BaseModel):
    name: str
    description: Union[str, None] = None
    price: int
