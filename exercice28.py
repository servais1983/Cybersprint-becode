car = {"brand": "Ford","model": "Mustang","year": 1964}
print(car["year"])  
for key in car:
    print(key)
for value in car.values():
    print(value)
for index, (key, value) in enumerate(car.items()):
    print(index, key, value)
new_dict = {f"cle_{i+1}": "car" for i in range(3)}
print(new_dict)
