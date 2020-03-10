from datetime import datetime, RECIPE_TYPE_LST


class BookException(Exception):
    def __init__(self, message):
        super().__init__(message)


class Book:
    def __init__(self, name):
        self.name = str(name)
        self.creation_date = datetime.now()
        self.last_update = self.creation_date
        self.recipes_list = {
            "starter": {},
            "lunch": {},
            "dessert": {}
        }

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        self.recipes_list[recipe.recipe_type][recipe.name] = recipe
        self.last_update = datetime.now()

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for recipe_type in RECIPE_TYPE_LST:
            if self.recipes_list[recipe_type][name]:
                print(self.recipes_list[recipe_type][name])
                return self.recipes_list[recipe_type][name]
        raise BookException(f"No recipe with the name {name}")

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if recipe_type not in RECIPE_TYPE_LST:
            raise BookException("Recipe type does not exist"
                                f" (must be: {', '.join(RECIPE_TYPE_LST)})")
        return self.recipes_list[recipe_type]
