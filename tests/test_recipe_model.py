from lib.recipe_model import RecipeModel

def test_it_constructs_with_all_four_attributes():
	test_recipe = RecipeModel(1, "test recipe name", 60, 5)

	assert test_recipe.id == 1
	assert test_recipe.name == "test recipe name"
	assert test_recipe.cooking_time == 60
	assert test_recipe.rating == 5

def test_its_repr_method_returns_formatted_str():
	test_recipe = RecipeModel(1, "test recipe name", 60, 5)

	assert str(test_recipe) == "RecipeModel(id=1, name='test recipe name', cooking_time=60, rating=5)"

def test_its_eq_returns_true_for_same_recipes():
	test_recipe1 = RecipeModel(1, "test recipe name", 60, 5)
	test_recipe2 = RecipeModel(1, "test recipe name", 60, 5)

	assert test_recipe1 == test_recipe2
