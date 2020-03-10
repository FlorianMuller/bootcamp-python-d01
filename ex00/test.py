from recipe import Recipe, RecipeException
from book import Book


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
        print(str(e))

    # Cooking level too low
    try:
        Recipe("Chocolate cake", -10, 45, ["chocolate", "flavour"], "dessert")
        print("~~~ ERROR ~~~")
    except RecipeException as e:
        print(str(e))

    # Cooking level not a number
    try:
        Recipe("Chocolate cake", "easy level omg", 45,
               ["chocolate", "flavour"], "dessert")
        print("~~~ ERROR ~~~")
    except RecipeException as e:
        print(str(e))

    # Negative cooking time
    try:
        Recipe("Chocolate cake", 2, -45, ["chocolate", "flavour"], "dessert")
        print("~~~ ERROR ~~~")
    except RecipeException as e:
        print(str(e))

    # Number Ingredient (not a lst)
    try:
        Recipe("Chocolate cake", 2, 45, 123456789, "dessert")
        print("~~~ ERROR ~~~")
    except RecipeException as e:
        print(str(e))

    # None ingredients
    try:
        Recipe("Chocolate cake", 2, 45, None, "dessert")
        print("~~~ ERROR ~~~")
    except RecipeException as e:
        print(str(e))

    # Wrong recipe type
    try:
        Recipe("Chocolate cake", 2, 45, ["chocolate", "flavour"], "Gouter")
        print("~~~ ERROR ~~~")
    except RecipeException as e:
        print(str(e))

    badCake = Recipe("Chocolate cake", 2, 45, [], "dessert", description=123)
    print(badCake.__dict__)


def test_book():
    grand_ma = Book("Grandma recipe collection")
    print(grand_ma.__dict__)


if __name__ == "__main__":
    # test_recipe()
    test_book()

    # Adding a recipe
    sandwich = Recipe("Chicken sandwich", 1, 5, ["salad", "tomato", "chicken",
                      "baguette"], "lunch", description="Easy to transport")
