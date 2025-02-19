from .recipe_model import RecipeModel

class RecipeRepo:
	def __init__(self, db_connection):
		self._connection = db_connection

	def all(self):
		rows = self._connection.execute("SELECT * FROM recipes")

		result = []
		for row in rows:
			item = RecipeModel(row["id"], row["name"], row["cooking_time"], row["rating"])
			result.append(item)

		return result
	
	
	def find(self, recipe_id):
		rows = self._connection.execute("SELECT * FROM recipes WHERE id = %s", [recipe_id])
		row = rows[0]

		result = RecipeModel(row["id"], row["name"], row["cooking_time"], row["rating"])

		return result