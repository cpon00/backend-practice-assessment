import json


class Recipes:
    DATA_FILE = './app/data.json'
    
    print(DATA_FILE)
    
    @classmethod
    def load(cls):
        with open(cls.DATA_FILE, 'r') as f:
            return json.load(f).get('recipes', [])
    
    @classmethod
    def write(cls, recipes: list):
        with open(cls.DATA_FILE, 'w') as f:
            return json.dump({'recipes': recipes}, f, indent=2)
    
    @classmethod
    def get_by_name(cls, recipes: list, name: str):
        return next((r for r in recipes if r.get('name') == name), None)
    
    @classmethod
    def update_recipe(cls, recipe: dict, new_data: dict):
        for key, val in new_data.items():
            recipe[key] = val
        
        