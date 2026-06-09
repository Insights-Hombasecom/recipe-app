# Recipe App CLI

A simple, persistent command-line recipe manager written in Python.

Store, view, add, and delete your favorite recipes — data is saved automatically to `recipes.json`.

## Features
- Add recipes with name, comma-separated ingredients, and multi-line instructions
- Delete recipes by name (case-insensitive)
- List all recipes with numbered, formatted output
- Data persists between sessions (JSON file)
- Graceful error handling and duplicate prevention

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/bundlab_/recipe-app.git
   cd recipe-app


   recipe-app/
├── recipe_app/         # Core package
│   ├── __init__.py
│   ├── models.py       # Recipe class
│   ├── storage.py      # JSON load/save
│   ├── app.py          # Business logic (add/delete)
│   └── cli.py          # User interface & menu
├── main.py             # Entry point
├── .venv/              # Virtual environment (ignored)
├── .gitignore
└── README.md