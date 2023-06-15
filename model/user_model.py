from typing import List, Optional
from pydantic import BaseModel


class UserAuth(BaseModel):
    email: str
    password: str


class UserPreferences(BaseModel):
    eat_halal: Optional[bool] = None
    allergies: Optional[List[str]] = None
    ingredients: Optional[List[str]] = None
    price_max: Optional[int] = None
    price_min: Optional[int] = None
