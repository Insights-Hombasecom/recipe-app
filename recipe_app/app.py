"""Core RecipeApp logic."""

from typing import List

from .models import Recipe
from .storage import load_recipes, save_recipes

class RecipeApp:
    def __init__(self, data_file: str = "recipes.json"):
        self.recipes: List[Recipe] = load_recipes(data_file)
        self.data_file = data_file

    def add_recipe(self, name: str, ingredients: List[str], instructions: List[str]):
        if not name:
            print("Recipe must have a name.")
            return
        if any(r.name.lower() == name.lower() for r in self.recipes):
            print("A recipe with that name already exists.")
            return
        recipe = Recipe(name=name, ingredients=ingredients, instructions=instructions)
        self.recipes.append(recipe)
        save_recipes(self.recipes, self.data_file)
        print(f"Added recipe '{name}'.")

    def delete_recipe(self, name: str):
        before = len(self.recipes)
        self.recipes = [r for r in self.recipes if r.name.lower() != name.lower()]
        if len(self.recipes) < before:
            save_recipes(self.recipes, self.data_file)
            print(f"Deleted recipe '{name}'.")
        else:
            print(f"No recipe named '{name}' was found.")

    # ... you can add edit/search/etc. methods here later
