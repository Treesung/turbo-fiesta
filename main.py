from fastapi import FastAPI
import uvicorn

app = FastAPI()

API_KEYS = ["alicealice", "joejoe1030"]

data = [
    {"name": "Pizza", "type": "Italian", "topping": "Pepperoni", "calories": 285},
    {"name": "Sushi", "type": "Japanese", "fish": "Salmon", "calories": 304},
    {"name": "Burger", "type": "American", "topping": "Cheese", "calories": 563},
    {"name": "Pasta", "type": "Italian", "sauce": "Tomato", "calories": 340},
    {"name": "Taco", "type": "Mexican", "filling": "Beef", "calories": 214},
    {"name": "Chocolate", "type": "Dessert", "flavor": "Dark", "calories": 150},
    {"name": "Sushi", "type": "Japanese", "fish": "Tuna", "calories": 184},
    {"name": "Curry", "type": "Indian", "spice level": "Medium", "calories": 325},
    {"name": "Salad", "type": "Healthy", "greens": "Kale", "calories": 120},
    {"name": "Steak", "type": "American", "cut": "Ribeye", "calories": 679},
    {"name": "Ice Cream", "type": "Dessert", "flavor": "Vanilla", "calories": 210},
    {"name": "Sushi", "type": "Japanese", "fish": "Eel", "calories": 372},
    {"name": "Taco", "type": "Mexican", "filling": "Chicken", "calories": 178},
    {"name": "Lasagna", "type": "Italian", "cheese": "Ricotta", "calories": 357},
    {"name": "Noodle Soup", "type": "Chinese", "noodles": "Udon", "calories": 280},
    {"name": "Crepes", "type": "French", "filling": "Strawberries", "calories": 231},
    {"name": "Fried Chicken", "type": "American", "style": "Southern", "calories": 390},
    {"name": "Mango", "type": "Fruit", "variety": "Alphonso", "calories": 150},
    {"name": "Shrimp Scampi", "type": "Italian", "sauce": "Garlic Butter", "calories": 332},
    {"name": "Pho", "type": "Vietnamese", "meat": "Beef", "calories": 450},
    ]

@app.get("/")
def home_route():
    return "this is my food analysis"

@app.get("/foodname")
async def get_names(api_key: str = None):
    if api_key in API_KEYS:
        names = []
        for food in data:
            names.append(food["name"])
        return names
    return "You Suck, You don'have permission to date Samuel Wu"

@app.get("/foodname/{name}")
async def get_person(name: str, api_key: str = None):
    if api_key in API_KEYS:
        for person in data:
            if name in person["name"]:
                return person
    return "You Suck"

if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", reload=True)
