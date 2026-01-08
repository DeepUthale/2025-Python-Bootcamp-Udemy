while True: # Make like when user press a certain key program stops - Done
    try:
        a = int(input("Enter the First Number : "))
        
        b = int(input("Enter the Second Number : "))
        
        print("What kind of operation do you want to perform. \nPress + for addition \nPress - for subtraction \nPress / for division \nPress * for multiplication")
        
        o = input("Enter Operation (or 'q' to quit): ")
        o = o.lower()
        if o == "q":
            print("Program exited.")
            break

        match o:
            case "+":
                print(f"The result is: {a + b}")
            case "-":
                print(f"The result is: {a - b}")
            case "/":
                print(f"The result is: {a / b}")
            case "*":
                print(f"The result is: {a * b}")
            case default:
                print(f"There was an error...")

    except Exception as e:
        print("Enter a valid value of a and b.")
