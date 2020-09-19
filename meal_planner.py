import json

food_database_path = './food_database.json'
food_database = json.load(food_database_path)

print(food_database)