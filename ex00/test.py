from recipe import Recipe, RecipeException
from book import Book, BookException
import time


def test_recipe():
    # Without description
    cake = Recipe("Chocolate cake", 2, 45, ["chocolate", "flavour"], "dessert")
    print(cake, end="\n\n")

    # With description
    sandwich = Recipe("Chicken sandwich", 1, 5, ["salad", "tomato", "chicken",
                      "baguette"], "lunch", description="Easy to transport")
    print(sandwich, end="\n\n")

    # ~~~~~~~~~~~~
    # Errors
    # ~~~~~~~~~~~~

    # Cooking level too high
    try:
        Recipe("Chocolate cake", 10, 45, ["chocolate", "flavour"], "dessert")
        print("~~~ ERROR ~~~")
    except RecipeException as e:
        print(e)

    # Cooking level too low
    try:
        Recipe("Chocolate cake", -10, 45, ["chocolate", "flavour"], "dessert")
        print("~~~ ERROR ~~~")
    except RecipeException as e:
        print(e)

    # Cooking level not a number
    try:
        Recipe("Chocolate cake", "easy level omg", 45,
               ["chocolate", "flavour"], "dessert")
        print("~~~ ERROR ~~~")
    except RecipeException as e:
        print(e)

    # Negative cooking time
    try:
        Recipe("Chocolate cake", 2, -45, ["chocolate", "flavour"], "dessert")
        print("~~~ ERROR ~~~")
    except RecipeException as e:
        print(e)

    # Number Ingredient (not a lst)
    try:
        Recipe("Chocolate cake", 2, 45, 123456789, "dessert")
        print("~~~ ERROR ~~~")
    except RecipeException as e:
        print(e)

    # None ingredients
    try:
        Recipe("Chocolate cake", 2, 45, None, "dessert")
        print("~~~ ERROR ~~~")
    except RecipeException as e:
        print(e)

    # Wrong recipe type
    try:
        Recipe("Chocolate cake", 2, 45, ["chocolate", "flavour"], "Gouter")
        print("~~~ ERROR ~~~")
    except RecipeException as e:
        print(e)

    badCake = Recipe("Chocolate cake", 2, 45, [], "dessert", description=123)
    print(badCake.__dict__)


def test_book():
    # New book
    grand_ma = Book("Grandma recipe collection")
    print(grand_ma.__dict__, end="\n\n")

    # Addin recipes
    time.sleep(.5)
    grand_ma.add_recipe(Recipe("Chocolate cake", 2, 45, ["chocolate",
                               "flavour"], "dessert"))
    grand_ma.add_recipe(Recipe("Apple pie", 3, 30, ["apple", "flavour"],
                               "dessert"))

    # Checking create and update time
    print("grand_ma.creation_date:", grand_ma.creation_date)
    print("grand_ma.last_update:", grand_ma.last_update, end="\n\n")

    # Recipe by type
    for rec in grand_ma.get_recipes_by_types("dessert").values():
        print(rec, end="\n\n")

    # Empty type
    print(grand_ma.get_recipes_by_types("lunch"), end="\n\n")

    # Recipe by name
    print(grand_ma.get_recipe_by_name("Apple pie").__dict__, end="\n\n")

    # ~~~~~~~~~~~~
    # Errors
    # ~~~~~~~~~~~~

    # Wrong recipe type
    try:
        grand_ma.get_recipes_by_types("panda")
        print("~~~ ERROR ~~~")
    except BookException as e:
        print(e)

    # Name doesn't exist
    try:
        grand_ma.get_recipe_by_name("Foie gras poilé")
        print("~~~ ERROR ~~~")
    except BookException as e:
        print(e)

    # Adding random things
    try:
        grand_ma.add_recipe("Fais les backs")
        print("~~~ ERROR ~~~")
    except BookException as e:
        print(e)


if __name__ == "__main__":
    test_recipe()

    print("\n\n=================\n\n")

    test_book()
