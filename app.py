from lib.database_connection import DatabaseConnection
from lib.recipe_repo import RecipeRepo


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/recipes_table.sql")

# Retrieve all artists
my_recipe_repo = RecipeRepo(connection)
my_recipes = my_recipe_repo.all()

# List them out
for recipe in my_recipes:
    print(recipe)
