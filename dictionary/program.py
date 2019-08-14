import json
import difflib

data = json.load(open("data.json"))


def translate():
    x = input("What would you like to look up? ")
    x = x.lower()
    x = difflib.get_close_matches(x, data.keys(), n=1)
    if x in data:
        return data[x]
    else:
        print("Word not found. Please enter again.")
        translate()


print(translate())

# x = difflib.get_close_matches("there is ej gnsdf", data)
# print(x[0])
