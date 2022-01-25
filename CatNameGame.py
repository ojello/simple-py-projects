# What are the names of all your cats! :D

catNames = []
while True:
    print(
        'please enter cat name, ( nothing to stop.): ')
    user_input = input()
    if user_input == '':
        break
    catNames = catNames + [user_input]  # list concatenation

print('My cat names are: ')
for user_input in catNames:
    print(' ' + user_input)
