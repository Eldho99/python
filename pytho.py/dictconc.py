#python program to concatinate 2 dictionary and create a new one . dict 1[name,age],dict 2 [city,gender]

dict1 = {
    "name": "John Doe",
    "age": 21
}

dict2 = {
    "city": "New York",
    "gender": "Male"
}


combined_dict = {**dict1, **dict2}

print(dict1)
print(dict2)


print("Combined Dictionary:", combined_dict)

