import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    close_match = get_close_matches(word, data.keys())
    if word in data:
        return data[word]
    elif len(close_match) > 0:
        print("Did you mean %s instead?" % close_match[0])
        user_confirmation = input("Y or N\n")
        if user_confirmation == 'Y':
            return data[close_match[0]]
        else:
            return "Please try again."

    else:
        print("Word not found. Please enter again.")
        translate()


x = input("What would you like to look up? ")
print(translate(x))
