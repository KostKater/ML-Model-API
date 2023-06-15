from datetime import date
from pydantic import BaseModel


class MealPlan(BaseModel):
    date: date
    meal_name: str
    group_meal: str
