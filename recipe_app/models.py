"""Data models for the recipe app."""

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
