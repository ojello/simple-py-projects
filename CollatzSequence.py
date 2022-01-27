# simplest impossible math problem aka Collatz sequence

def collatz(number):
    if number % 2 == 0:
        value = number // 2
        return value
    elif number % 2 == 1:
        value = 3 * number + 1
        return value

while True:
    try:
        user_input = int(input('please enter integer: '))
        if collatz(user_input) != 1:
            print(collatz(user_input))
        elif collatz(user_input) == 1:
            break 
    except ValueError:
        print(' Invalid value. Actually enter a real integer >:(')
