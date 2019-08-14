import json

data = json.load(open("data.json"))


def translate():
    x = input("What would you like to look up? ")
    if x in data:
        return data[x]
    else:
        print("Word not found. Please enter again.")
        translate()


print(translate())
