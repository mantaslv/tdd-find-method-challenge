from lib.recipe_repo import RecipeRepo
from lib.recipe_model import RecipeModel

def test_its_all_fn_returns_list_of_all_recipes(db_connection):
	db_connection.seed("seeds/recipes_table.sql")
	test_recipe_repo = RecipeRepo(db_connection)

	result = test_recipe_repo.all()

	assert result == [
		RecipeModel(1, 'Apple Pie', 90, 4),
		RecipeModel(2, 'Frozen Pizza', 12, 2),
		RecipeModel(3, 'Tortelloni', 3, 3),
		RecipeModel(4, 'Egg Fried Rice', 20, 3)
	]

def test_its_find_fn_search_by_id_returns_recipe_model_obj(db_connection):
	db_connection.seed("seeds/recipes_table.sql")
	test_recipe_repo = RecipeRepo(db_connection)

	result = test_recipe_repo.find(recipe_id=3)

	assert result == RecipeModel(3, 'Tortelloni', 3, 3)