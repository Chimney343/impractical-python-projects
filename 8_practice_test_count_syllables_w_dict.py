"""
8_practice_test_count_syllables_w_dict.py

"SYLLABLE COUNTER VS. DICTIONARY FILE"
This is a practice project from chapter 8 of "Impractical Python Projects" by Lee Vaughan.

GOAL:
Write a Python program that lets you test count_syllables.py (or any other syllablecounting Python code) against a
dictionary file. After allowing the user to specify how many words to check, choose the words at random and display a
listing of each word and its syllable count on separate lines.
"""
# GLOBAL PARAMETERS
args = {
    # Enter the name of dictionary text file
    'dictionary': '2of4brif.txt'
}
# IMPORTS
import sys
import random
import json
from load_dictionary import load
from count_syllables import count_syllables
from nltk.corpus import cmudict
cmudict = cmudict.dict()

def main():
    dictfile = load(args['dictionary'])
    len_dictfile = len(dictfile)
    with open('missing_words.json') as f:
        missing_words = json.load(f)
    print("Welcome to Dictionary Syllable Counter.")
    print("Enter the number of random words to count syllables for, else press Enter to exit:")
    while True:
        n_words = input()
        if n_words == '':
            sys.exit(1)
        if not n_words.isdigit():
            print("Enter the number instead of a character.")
        if int(n_words) > len_dictfile:
            print("Sample size larger than dictionary. Pick a smaller number.")
            continue
        words = random.sample(dictfile, int(n_words))
        for word in words:
            try:
                num_syllables = count_syllables(word)
                print("{}: {}".format(word, num_syllables))
            except KeyError:
                print("{} not found.".format(word), file=sys.stderr)

if __name__ == "__main__":
    main()




