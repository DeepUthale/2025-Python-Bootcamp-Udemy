# Decorator is a function that takes a function, it creates a new function inside its body (wrapper). Then it returns that new function

def decorator(func):
    def wrapper():
        print("I am about to execute a function...")
        func()
        print("I have executed this function...")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()

# say_hello()
# fu = decorator(say_hello)
# fu

'''
fu will look something like this
def fu():
    print("I am about to execute a function...")
    func()
    print("I have executed this function...")
'''
