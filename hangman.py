# randomly generate a word - use a generator for this
# have the user guess a letter or a word in each round
# if user runs out of 6 guesses, you lose the game
# if a user guesses a letter, letter show up and user gets to guess again and as long as guesses < 6

# # Generates a random number between a given positive range.

import urllib.request
import random

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = urllib.request.urlopen(word_site)
txt = response.read()
words = txt.splitlines()

# randomly chooses a word from the list
random_word = (random.choice(words))
print(random_word)


# using list function to split word into letters
list_of_letters = list(random_word)
print(list_of_letters)


# converting ascii to characters
ascii_convert = ''.join(chr(i) for i in list_of_letters)
print(ascii_convert)


def split_word(word):
    return [char for char in word]


word_array = split_word(ascii_convert)
print(word_array)

censored = '*' * len(list_of_letters)
print(censored)

# take what user has, convert it into a  character
# check the character to every character in the word array


def list_duplicates_of(b, a):
    if [idx for idx in range(len(b)) if b[idx] == a]:
        number = []
        number += b
        # number += str(b.index(a))
    return print(number)

    for index in range(len(b)):
        if a == b[index]:
            number = []
            number += index
            print(number)

# if there is a match, then you need to save the index of the match as a variable, "number"
# then say censored.charAt("number") = a, print(censored)


a = str(input('please enter a character: '))
b = word_array
print(list_duplicates_of(b, a))


# def user_attempt():
#     while True:
#         user_guess = str(input('please guess a letter or word: '))  # see this
#         try:
#             #            user_guess = str(input('please guess a letter or word'))
#             if user_guess.isalpha():
#                 break
#             else:
#                 raise TypeError
#         except TypeError:
#             print('letters only please')
#             continue
#         except EOFError:
#             print('Please input a letter or word!')
#             user_guess
#             continue


# user_attempt()
