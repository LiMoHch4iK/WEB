import json

cats_dict = [
  {
    "name": "Barsik",
    "age": 7,
    "meals": [
      "Wiskas",
      "Royal Canin",
      "Purina",
      "Hills",
      "Brit Care"
    ]
  },
  {
    "name": "Mursik",
    "age": 3,
    "meals": [
      "Purina",
      "Hills",
      "Brit Care"
    ]
  }
]

with open('cats_3.json', 'w') as cat_file:
    json.dump(cats_dict, cat_file, indent=4)