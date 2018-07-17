import json
from difflib import get_close_matches

data=json.load(open("data.json",'r'))
def find(w):
    w=w.lower()
    if w in data:
            return data[w]
    elif  len(get_close_matches(w,data.keys()))>0:
        optn=input("Did you mean {} instead of {}. Enter 'Y' for yes or 'N' for no".format(get_close_matches(w,data.keys())[0],w))
        if optn=='Y':
                return data[get_close_matches(w,data.keys())[0]]
        elif optn=='N':
                return "The given word doesn't exist"
        else:
                return "wrong input....we didn't understand"
    else:
            return "The given word doesn't exist"


word=input("Enter the word: ")
output=find(word)
if type(output)==list:
    for i in output:
        print(i)
else:
    print(output)
