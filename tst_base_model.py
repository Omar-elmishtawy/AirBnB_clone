#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
model_json = my_model.to_dict()
print(model_json)
print("JSON of my_model:")
for key in model_json.keys():
    print("{}: ({}) - {}".format(key, type(model_json[key]), model_json[key]))
