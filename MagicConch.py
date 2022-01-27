# Ask the Magic Conch what they think and maybe they will give the answer you desire!
import random
import sys

# if the magic conch feels like it has been asked too many times, it quits the session
# you have asked too many questions, be gone peasant!

while True:
    while True:
        user_input = input(str(
            'Ask the Magic Conch a question, and maybe they will give you the answer you desire or (q)uit:'))
        if user_input == 'q':
            print('see you next time when your fortune awaits~')
            sys.exit()
        else:
            break

    def get_response(answer):
        if answer == 1:
            return print('Maybe so...')

        elif answer == 2:
            return print('Definitely Yes')

        elif answer == 3:
            return print('I do not know..')

        elif answer == 4:
            return print('Ask me tomorrow, when you aren''t my time!')

        elif answer == 5:
            return ('What do you think?')

        elif answer == 6:
            return print('No')

        elif answer == 7:
            return print('It is decidely so')

        elif answer == 8:
            return print('Maybe ask a better question!')

        elif answer == 9:
            return print('Highly doubtful!')

        elif answer == 10:
            return print('Most likely never')

    answer = random.randint(1, 10)

    fortune = get_response(answer)
    count = 0

    for x in get_response(answer):
        count += 1
        print(count)

    # patience = random.randint(1, 7)

    # if question_count < patience:
    # continue the game

    # elif question_count == patience:
    #     print('Be gone Peasant!! you have asked too many questions!')

    # patience = random.randint(1, 10)

    # if question_count < patience:
    #     # continue the game
    # elif question_count == patience:
    #     print('Be gone Peasant! you have asked too much questions. Come another day')
