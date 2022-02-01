# dog py


class Dog:
    def __init__(self, name, age, size, breed, sex):
        self.name = name
        self.age = age
        self.size = size
        self.breed = breed
        self.sex = sex
        print('dog initialized')


# first method - bark
# methods are defined as their own named unctions
# remember to put the self parameter every time

    def bark(self):
        print('woof!')


# instantation call that creates a Dog object:
dogOne = Dog('Rex', 4, '20 cm', 'mutt', ',male')

print(dogOne)
print(dogOne.breed)

# calling method - bark
dogOne.bark()
