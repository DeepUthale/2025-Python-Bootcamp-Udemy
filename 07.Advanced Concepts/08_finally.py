def divide(a, b):
    try:
        c = a/b
        print(c)
        return c
        
    except Exception as e:
        print(e)
        return None

    # This is always executed no matter if they completely executes or not
    finally:
        print("This is Always Executed")

a = int(input("Enter number 1 : "))
b = int(input("Enter number 2 : "))
divide(a, b)
