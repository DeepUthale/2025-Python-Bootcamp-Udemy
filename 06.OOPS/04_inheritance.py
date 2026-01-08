class Animal: # Parent class (superclass)
    location = "Australia"
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Speaking now...")

class Dog(Animal): #This is how Inheritance is done in python
    def speak(self):
        super().speak()
        print("Woof!")

# a = Animal("Dog")
# a.speak()

d = Dog("Bruno")
d.speak()

print(d.location)
