def cookbook(*recipes_data):
    recipes_dict = {}

    for recipe in recipes_data:
        current_name, cuisine, ingredients = recipe
        recipe_info = {"name": current_name, "ingredients": ingredients}

        if cuisine not in recipes_dict:
            recipes_dict[cuisine] = []

        recipes_dict[cuisine].append(recipe_info)

    sorted_cuisines = sorted(recipes_dict.keys(), key=lambda x: (-len(recipes_dict[x]), x))
    sorted_cookbook = {cuisine: sorted(recipes_dict[cuisine], key=lambda x: x['name']) for cuisine in sorted_cuisines}
    result = ""

    for cuisine, recipes in sorted_cookbook.items():
        result += f"{cuisine} cuisine contains {len(recipes)} recipes:\n"
        for recipe in recipes:
            result += f"  * {recipe['name']} -> Ingredients: {', '.join(el for el in recipe['ingredients'])}\n"

    return result


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
