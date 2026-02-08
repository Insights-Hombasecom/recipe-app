"""Entry point for the recipe app."""

from recipe_app.app import RecipeApp
from recipe_app.cli import read_multiline, display_recipes, show_menu

def main():
    app = RecipeApp()
    try:
        while True:
            choice = show_menu()
            if choice == "1":
                name = input("Enter recipe name: ").strip()
                raw_ings = input("Enter ingredients (comma-separated): ").strip()
                ingredients = [i.strip() for i in raw_ings.split(",") if i.strip()]
                instructions = read_multiline(
                    "Enter instructions, one per line. Type 'done' on its own line when finished:"
                )
                app.add_recipe(name, ingredients, instructions)
            elif choice == "2":
                name = input("Enter recipe name to delete: ").strip()
                app.delete_recipe(name)
            elif choice == "3":
                display_recipes(app.recipes)
            elif choice == "4":
                print("Goodbye.")
                break
            else:
                print("Invalid choice. Please try again.")
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")

if __name__ == "__main__":
    main()
