def marks(**kwargs):
    # Kwargs is a dictonary with all the key value pairs which were passed to marks 
    for item in kwargs.keys():
        print(f"The Marks of {item} is {kwargs[item]}")

marks(Shubham = 34, Vikrant = 54, Jack = 34, Marie = 90, Priya = 45)
