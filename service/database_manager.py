from service.config import db
from datetime import datetime, date


def read_users_collection():
    users_ref = db.collection("users")
    docs = users_ref.stream()
    users_list = []

    for doc in docs:
        user_data = doc.to_dict()
        users_list.append(user_data)

    return users_list


def read_user_doc(email):
    doc_ref = db.collection("users").document(email)
    doc = doc_ref.get()
    return doc.to_dict()


def create_user_doc(email):
    data = {
        "email": email,
        "eat_halal": True,
        "allergies": [],
        "ingredients": [],
        "price_min": 0,
        "price_max": 999999999
    }

    db.collection("users").document(email).set(data)


def update_user_doc(email, eat_halal, allergies, ingredients, price_min, price_max):
    doc_ref = db.collection("users").document(email)
    if eat_halal is not None:
        doc_ref.update({"eat_halal": eat_halal})
    if allergies is not None:
        allergies = [item.lower() for item in allergies]
        doc_ref.update({"allergies": allergies})
    if ingredients is not None:
        ingredients = [item.lower() for item in ingredients]
        doc_ref.update({"ingredients": ingredients})
    if price_min is not None:
        doc_ref.update({"price_min": price_min})
    if price_max is not None:
        doc_ref.update({"price_max": price_max})


def create_meal_plan(email, date, name, group):
    timestamp = datetime.strptime(str(date), "%Y-%m-%d").timestamp()
    doc_ref = db.collection(
        "users").document(email).collection("mealplans").document(str(int(timestamp)))
    doc = doc_ref.get()
    if doc.exists:
        if group == "breakfast":
            doc_ref.update({"breakfast": name})
        elif group == "lunch":
            doc_ref.update({"lunch": name})
        elif group == "dinner":
            doc_ref.update({"dinner": name})
    else:
        if group == "breakfast":
            data = {
                "date_in_timestamp": timestamp,
                "breakfast": name,
                "lunch": "",
                "dinner": "",
            }
        elif group == "lunch":
            data = {
                "date_in_timestamp": timestamp,
                "breakfast": "",
                "lunch": name,
                "dinner": "",
            }
        elif group == "dinner":
            data = {
                "date_in_timestamp": timestamp,
                "breakfast": "",
                "lunch": "",
                "dinner": name,
            }
        doc_ref.set(data)



def read_meal_plan(email):
    user_meal_plans_ref = db.collection(
        "users").document(email).collection("mealplans")
    docs = user_meal_plans_ref.stream()
    meal_plans_list = []
    current_date = date.today()
    timestamp = datetime.strptime(str(current_date), "%Y-%m-%d").timestamp()
    for doc in docs:
        meal_plan = doc.to_dict()
        meal_plan["date_in_timestamp"] = datetime.fromtimestamp(
            meal_plan["date_in_timestamp"]).strftime("%Y-%m-%d")
        meal_plans_list.append(meal_plan)
        # meal_plan_obj = {}
        # num = meal_plan["date_in_timestamp"]
        # meal_plan_obj[num] = meal_plan
        # meal_plans_list.append(meal_plan_obj)

    return meal_plans_list

def read_meal_plan_doc(email, date):
    timestamp = datetime.strptime(str(date), "%Y-%m-%d").timestamp()
    doc_ref = db.collection(
        "users").document(email).collection("mealplans").document(str(int(timestamp)))
    doc = doc_ref.get()
    return doc.to_dict()