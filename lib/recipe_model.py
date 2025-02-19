class RecipeModel:
	def __init__(self, id, name, cooking_time, rating):
		self.id = id
		self.name = name
		self.cooking_time = cooking_time
		self.rating = rating

	def __repr__(self):
		attrs = [f"{attr}={value!r}" for attr, value in self.__dict__.items()]
		attrs_str = ", ".join(attrs)
		return f"RecipeModel({attrs_str})"
	
	def __eq__(self, other):
		return self.__dict__ == other.__dict__