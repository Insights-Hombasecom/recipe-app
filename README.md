# Recipe App CLI

A clean, persistent command-line recipe manager built in Python.

Easily store, view, add, and delete your favorite recipes. All data is automatically saved to `recipes.json` and persists between sessions.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Features

- **Add recipes** with name, ingredients (comma-separated), and multi-line instructions
- **Delete recipes** by name (case-insensitive)
- **List all recipes** with clean, numbered formatting
- **Persistent storage** using JSON — no database required
- **Duplicate prevention** and graceful error handling
- Simple, intuitive menu-driven interface

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/bundlab_/recipe-app.git
   cd recipe-app
   ```

2. (Optional but recommended) Create and activate a virtual environment:Bash
   ```bash python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS / Linux
   source .venv/bin/activate
   ```
## Project Structure
   ```plaintext recipe-app/
├── recipe_app/         # Core package
│   ├── __init__.py
│   ├── models.py       # Recipe class
│   ├── storage.py      # JSON load/save
│   ├── app.py          # Business logic (add/delete)
│   └── cli.py          # User interface & menu
├── main.py             # Entry point
├── .venv/              # Virtual environment (ignored)
├── .gitignore
└── README.
   ```
## Usage
Once you run python main.py, you'll see a clean menu:
```text 
Recipe App CLI
==============

1. Add a new recipe
2. List all recipes
3. Delete a recipe
4. Exit
```

- Add Recipe: Enter name, ingredients (e.g. chicken, rice, soy sauce), and instructions (multi-line, end with blank line).
- List Recipes: View all saved recipes with nicely formatted output.
- Delete Recipe: Type the recipe name (case-insensitive).

## Example
Adding a recipe:
```text
Recipe Name: Butter Chicken
Ingredients (comma-separated): chicken, butter, tomato sauce, cream, spices
Instructions:
Marinate the chicken...
Cook the sauce...
<press Enter on empty line to finish>
```
## Technologies Used
Python 3.8+
JSON for data persistence
No external dependencies

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## License
This project is licensed under the MIT License.

## Made with ❤️ for home cooks who love the terminal.

### Key Improvements Made:
- **Professional tone** and cleaner layout
- Added badges for visual appeal
- Clear installation steps with virtual environment
- Better project structure visualization
- Usage section with example
- Added `requirements.txt` mention (you can remove if not needed)
- Consistent formatting and spacing
- Call-to-action at the bottom

Would you like me to also generate a more advanced version with screenshots (via ASCII art or pla
