"""A simple recipe app CLI with persistent storage.

Features:
- Add, delete, and display recipes
- Persist recipes to `recipes.json`
"""

import json
import os
from typing import List


class Recipe:
    def __init__(self, name: str, ingredients: List[str], instructions: List[str]):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def to_dict(self):
        return {
            "name": self.name,
            "ingredients": self.ingredients,
            "instructions": self.instructions,
        }


class RecipeApp:
    def __init__(self, data_file: str = "recipes.json"):
        self.recipes: List[Recipe] = []
        self.data_file = data_file
        self.load_recipes()

    def load_recipes(self):
        if not os.path.exists(self.data_file):
            return
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            for item in data:
                r = Recipe(
                    name=item.get("name", ""),
                    ingredients=item.get("ingredients", []),
                    instructions=item.get("instructions", []),
                )
                self.recipes.append(r)
        except Exception:
            # If loading fails, start with empty list (avoid crash on corrupt file)
            self.recipes = []

    def save_recipes(self):
        data = [r.to_dict() for r in self.recipes]
        try:
            with open(self.data_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving recipes: {e}")

    def add_recipe(self, name: str, ingredients: List[str], instructions: List[str]):
        if not name:
            print("Recipe must have a name.")
            return
        # prevent duplicate names
        if any(r.name.lower() == name.lower() for r in self.recipes):
            print("A recipe with that name already exists.")
            return
        r = Recipe(name=name, ingredients=ingredients, instructions=instructions)
        self.recipes.append(r)
        self.save_recipes()
        print(f"Added recipe '{name}'.")

    def delete_recipe(self, name: str):
        before = len(self.recipes)
        self.recipes = [r for r in self.recipes if r.name.lower() != name.lower()]
        if len(self.recipes) < before:
            self.save_recipes()
            print(f"Deleted recipe '{name}'.")
        else:
            print(f"No recipe named '{name}' was found.")

    def display_recipes(self):
        if not self.recipes:
            print("No recipes available.")
            return
        for idx, r in enumerate(self.recipes, start=1):
            print(f"{idx}. {r.name}")
            print("   Ingredients:")
            for ing in r.ingredients:
                print(f"     - {ing}")
            print("   Instructions:")
            for step_no, step in enumerate(r.instructions, start=1):
                print(f"     {step_no}. {step}")
            print()


def _read_multiline(prompt: str) -> List[str]:
    print(prompt)
    lines: List[str] = []
    while True:
        line = input()
        if line.strip().lower() == "done":
            break
        lines.append(line.strip())
    return [l for l in lines if l]


def main():
    app = RecipeApp()
    try:
        while True:
            print("\nRecipe App")
            print("1. Add Recipe")
            print("2. Delete Recipe")
            print("3. Display Recipes")
            print("4. Quit")
            choice = input("Enter your choice (1-4): ").strip()
            if choice == "1":
                name = input("Enter recipe name: ").strip()
                raw_ings = input("Enter ingredients (comma-separated): ").strip()
                ingredients = [i.strip() for i in raw_ings.split(",") if i.strip()]
                instructions = _read_multiline("Enter instructions, one per line. Type 'done' on its own line when finished:")
                app.add_recipe(name, ingredients, instructions)
            elif choice == "2":
                name = input("Enter recipe name to delete: ").strip()
                app.delete_recipe(name)
            elif choice == "3":
                app.display_recipes()
            elif choice == "4":
                print("Goodbye.")
                break
            else:
                print("Invalid choice. Please try again.")
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")


if __name__ == "__main__":
    main()