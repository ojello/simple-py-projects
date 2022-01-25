import random

random_number = random.randint(1, 100)

print(random_number)

print('I am thinking of a number between 1 and 100')

guess_count = 0

while True:
    user_input = input('Guess a number between 1 and 100')
    user_guess = int(user_input)
    if user_guess < random_number:
        print('your guess is too low')
        guess_count += 1
        print('current guess count is ' + str(guess_count))
        # user_input = input('Take a guess:')
    elif user_guess > random_number:
        print('your guess is too high')
        guess_count += 1
        print('current guess count is ' + str(guess_count))
        # user_input = input('Take a guess:')
    else:
        break

if user_guess == random_number:
    print('you guessed my number after ' + str(guess_count) + ' attempts!  :D')
