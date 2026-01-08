while True:
    # try:
    #     a = int(input("Enter number 1 : "))
    #     b = int(input("Enter number 2 : "))

    #     print(f"The Division is {a / b}")
    
    # except ValueError:
    #     print("Please don't perform bad typecasts...")
    # except ZeroDivisionError:
    #     print("Hey don't divide by 0...")
    # except Exception as e:
    #     print("Something went wrong...", e)

    a = int(input("Enter number 1 : "))
    b = int(input("Enter number 2 : "))
    
    if b == 0:
        raise ValueError("Please don't divide by 0 : ")
 
