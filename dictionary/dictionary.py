import json
import difflib
from difflib import get_close_matches

def load_dict():
    dict = json.load(open("data.json"))
    return dict

def get_input_word():
    word = input("What word do you want to look up? ")
    return word

def find_close_match(dict,word):
    matches = get_close_matches(word, dict.keys())
    if matches:
        word = input("Found the following close matches, type the word you really want" + str(matches))
        return word
    else:
        print("found no close match")
        return ""

def print_def(definitions):
    i = 1
    for definition in definitions:
        print("Definition " + str(i)+ ":" + definition)
        i=i+1


def get_def(dict, word):
    if word.lower() in dict:
        print_def(dict[word])
    elif word.title() in dict:
        print_def(dict[word.title()])
    else:
        close_match = find_close_match(dict,word)
        if len(close_match) > 0:
            print_def(dict[close_match])
        else:
            print("didn't find the word")

dict = load_dict()
word = get_input_word()
get_def(dict,word)
