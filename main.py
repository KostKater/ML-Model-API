from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from model.user_model import UserAuth, UserPreferences
from model.meal_model import MealPlan
from model.ml.ml_model import recommend_meals, all_meals, recipe_meal
from service.config import auth
from service.database_manager import read_users_collection, read_user_doc, create_user_doc, update_user_doc, read_meal_plan, read_meal_plan_doc, create_meal_plan
from os import environ as env
import re

app = FastAPI()
security = HTTPBearer()


def is_email_valid(email):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if (re.fullmatch(email_regex, email)):
        return True
    return False


@app.get("/")
def index():
    return {"greetings": "Hi! Welcome to KostKater Back-End App"}


@app.get("/check")
async def check_environment():
    try:
        user_list = read_users_collection()
        # return {"userList": user_list}
        return {"env": f"This is in {env['ENV']} environment", "userList": user_list}
    except Exception as error:
        return {
            "error": True,
            "message": ("An error occurred:", str(error))
        }


@app.post("/login")
async def login(userAuth: UserAuth):
    try:
        if not is_email_valid(userAuth.email):
            return {
                "error": True,
                "message": "Format email tidak valid"
            }
        user = auth.sign_in_with_email_and_password(
            userAuth.email, userAuth.password)
        return {"error": False,
                "message": "Login berhasil!",
                "userInfo": {
                    "email": user["email"],
                    "token": user["idToken"]
                }}
    except:
        return {
            "error": True,
            "message": "Email atau password tidak sesuai"
        }


@app.post("/register")
async def register(userAuth: UserAuth):
    try:
        if not is_email_valid(userAuth.email):
            return {
                "error": True,
                "message": "Format email tidak valid"
            }
        user = auth.create_user_with_email_and_password(
            userAuth.email, userAuth.password)
        create_user_doc(userAuth.email)
        return {"message": "Registrasi berhasil!",
                "userInfo": {
                    "email": user["email"],
                    "token": user["idToken"]
                }}
    except:
        return {
            "error": True,
            "message": "Proses registrasi gagal, email sudah digunakan"
        }


@app.get("/user/data")
async def get_user_data(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        token = credentials.credentials
        user = auth.get_account_info(token)
        email = user["users"][0]["email"]
        user_data = read_user_doc(email)
        return {"data": user_data}
    except Exception as error:
        return {
            "error": True,
            "message": ("An error occurred:", str(error))
        }


@app.post("/user/data")
async def update_user_data(userPreferences: UserPreferences, credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        token = credentials.credentials
        user = auth.get_account_info(token)
        email = user["users"][0]["email"]
        update_user_doc(email, userPreferences.eat_halal,
                        userPreferences.allergies, userPreferences.ingredients, userPreferences.price_min, userPreferences.price_max)
        user_data = read_user_doc(email)
        return {"data": user_data}
    except Exception as error:
        return {
            "error": True,
            "message": ("An error occurred:", str(error))
        }


@app.get("/meals/all")
async def get_all_meals(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        meals_data = all_meals()
        return {"data": meals_data}
    except Exception as error:
        return {
            "error": True,
            "message": ("An error occurred:", str(error))
        }


@app.get("/meals/recommend")
async def get_meals_recommendation(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        token = credentials.credentials
        user = auth.get_account_info(token)
        email = user["users"][0]["email"]
        user_data = read_user_doc(email)

        if user_data["eat_halal"]:
            is_halal = '1'
        else:
            is_halal = '0'
        allergies = ",".join(user_data["allergies"])
        ingredients = user_data["ingredients"]
        price_min = user_data["price_min"]
        price_max = user_data["price_max"]

        meals_data = recommend_meals(
            ingredients, allergies, is_halal, price_min, price_max, ingredients)

        return {"data": meals_data}
    except Exception as error:
        return {
            "error": True,
            "message": ("An error occurred:", str(error))
        }


@app.get("/recipe")
async def get_meal_recipe(name: str, credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        recipe = recipe_meal(name)
        return {"data": recipe}
    except Exception as error:
        return {
            "error": True,
            "message": ("An error occurred:", str(error))
        }


@app.get("/user/mealplan")
async def get_meal_plan(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    user = auth.get_account_info(token)
    email = user["users"][0]["email"]
    mealPlan = read_meal_plan(email)
    return {"data": mealPlan}


@app.post("/user/mealplan")
async def post_meal_plan(mealPlan: MealPlan, credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    user = auth.get_account_info(token)
    email = user["users"][0]["email"]
    create_meal_plan(email, mealPlan.date,
                     mealPlan.meal_name, mealPlan.group_meal)
    meal_plan = read_meal_plan_doc(email, mealPlan.date)
    return {"data": meal_plan}
