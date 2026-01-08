def very_slow_function():
    print("Something...")
    print("Something...")
    print("Something...")
    print("Something...")
    print("Something...")
    print("Something...")
    return 70

# a = very_slow_function()
if ((a := very_slow_function()) > 10):
    print(a)
else:
    print("It's Not Greater Than 10")


while(data := input("Enter the Value : ")):
    print(data)
    if data == "q":
        break
