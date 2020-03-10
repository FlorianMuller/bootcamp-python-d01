class RecipeException(Exception):
    def __init__(self, message):
        super().__init__(message)


RECIPE_TYPE_LST = ["starter", "lunch", "dessert"]


class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time,
                 ingredients, recipe_type, description=None):
        # Name
        self.name = str(name)

        # Cooking level
        try:
            if not 1 <= int(cooking_lvl) <= 5:
                raise RecipeException("Bad cooking level")
            self.cooking_lvl = int(cooking_lvl)
        except ValueError:
            raise RecipeException("Cooking level must be a number")

        # Cooking time
        try:
            if int(cooking_time) < 0:
                raise RecipeException("Cooking time can't be negative")
            self.cooking_time = cooking_time
        except ValueError:
            raise RecipeException("Cooking time must be a number")

        # Ingredients
        try:
            self.ingredients = [str(ing) for ing in list(ingredients)]
        except TypeError:
            raise RecipeException("Ingredients must be a list")

        # Recipe type
        if recipe_type not in RECIPE_TYPE_LST:
            raise RecipeException(
                    "Recipe type does not exist"
                    f" (must be: {', '.join(RECIPE_TYPE_LST)})"
            )
        self.recipe_type = str(recipe_type)

        # Description
        self.description = (description and str(description)) or ""

    def __str__(self):
        text = (
            f"{self.name}: [{self.recipe_type}]\n"
            f"  - Cooking level: "
            f"{'•' * self.cooking_lvl}{'○' * (5 - self.cooking_lvl)}\n"
            f"  - Cooking time: {self.cooking_time} minutes\n"
            f"  - Ingredients: {', '.join(self.ingredients)}"
        )

        text += (f"\n  - Description: {self.description}"
                 if self.description else "")
        return text
