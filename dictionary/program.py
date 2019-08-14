import json

data = json.load(open("data.json"))


def translate(x):
    return data[x]


word = input("What would you like to look up? ")

print(translate(word))
