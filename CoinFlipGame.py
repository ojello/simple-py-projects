# CoinFlip Game is a program to find out how often a streak of six heads or a streak of six tails come up in a randomly generated list of heads and tails

# first first part: generate a list of randomly selected 'heads' and 'tails' values
# second part: checks if there is a streak in it
# put all of this code in a loop that repeats the experiement 10,000 times so we can find out what percentage of the coin flips contain a streak of six heads or tails in a row.

# the function call random.randint(-0, 1) will return a o value of 50% of the time and a 1 value the other 50% of the time.
import random
numberOfStreaks = 0

for experimentNumber in range(10000):
    random_list = []
    for i in range(1, 101):
        # return a value of 0 50% and 1 50% of the time
        randomNumber = random.randint(0, 1)
        if randomNumber == 1:
            computer_choice = 'H'
            random_list = random_list + [computer_choice]
        elif randomNumber == 0:
            computer_choice = 'T'
            random_list = random_list + [computer_choice]
print(random_list)
# for i in random_list:
#     print('hello')


# Code that checks if there is a streak of 6 heads or tails in a row


# for experimentNumber in range(10000):
# Code that checks if there is a streak of 6 heads or tails in a row.
# print('Chance of streak: %s%%' % (numberOfStreaks / 100))
