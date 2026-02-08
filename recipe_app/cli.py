"""CLI user interaction: menu, inputs, display."""

from typing import List

from .models import Recipe

def read_multiline(prompt: str) -> List[str]:
    print(prompt)
    lines: List[str] = []
    while True:
        line = input()
        if line.strip().lower() == "done":
            break
        if line.strip():
            lines.append(line.strip())
    return lines

def display_recipes(recipes: List[Recipe]):
    if not recipes:
        print("No recipes available.")
        return
    for idx, r in enumerate(recipes, start=1):
        print(f"{idx}. {r.name}")
        print("   Ingredients:")
        for ing in r.ingredients:
            print(f"     - {ing}")
        print("   Instructions:")
        for step_no, step in enumerate(r.instructions, start=1):
            print(f"     {step_no}. {step}")
        print()

def show_menu() -> str:
    print("\nRecipe App")
    print("1. Add Recipe")
    print("2. Delete Recipe")
    print("3. Display Recipes")
    print("4. Quit")
    return input("Enter your choice (1-4): ").strip()
