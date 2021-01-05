from pydantic import BaseModel
from typing import Optional


class RandomWordData(BaseModel):
    quantity: Optional[int]
    start_with: Optional[str]