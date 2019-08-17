import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    close_match = get_close_matches(word, data.keys())
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(close_match) > 0:
        print("Did you mean %s instead?" % close_match[0])
        user_confirmation = input("Y or N\n")
        if user_confirmation == 'Y':
            return data[close_match[0]]
        elif user_confirmation == 'N':
            return "The word doesn't exist. Please double check."
        else:
            return "The word doesn't exist. Please try again"

    else:
        return "Word not found. Please enter again."


x = input("What would you like to look up? ")

output = translate(x)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
