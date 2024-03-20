# A class that defines a person

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

# A method to introduce the person
    def introduce(self):
        print('Your name is:' + self.name) 
        print('Your age is:' , self.age)
        print('Your gender is:' + self.gender)

# An instance of the person and the result of calling introduce on the person object
person = Person("Stephen",50, "male")
person.introduce()