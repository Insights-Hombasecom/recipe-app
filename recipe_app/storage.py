"""Persistence layer: load/save recipes to JSON."""

import json
import os
from typing import List

from .models import Recipe

def load_recipes(data_file: str = "recipes.json") -> List[Recipe]:
    if not os.path.exists(data_file):
        return []
    try:
        with open(data_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [
            Recipe(
                name=item.get("name", ""),
                ingredients=item.get("ingredients", []),
                instructions=item.get("instructions", []),
            )
            for item in data
        ]
    except Exception:
        return []

def save_recipes(recipes: List[Recipe], data_file: str = "recipes.json") -> None:
    data = [r.to_dict() for r in recipes]
    try:
        with open(data_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving recipes: {e}")
