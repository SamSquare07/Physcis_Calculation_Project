reaction = input("Enter what you want to get (v/u/a/t) : ")

if reaction == "v" or reaction == "u" or reaction == "a" or reaction == "t":
    while reaction == "v" or reaction == "u" or reaction == "a" or reaction == "t":
        try:
            if reaction == "v":
                while reaction == "v":
                    try:
                        u = float(input("Enter your u : "))
                        a = float(input("Enter your a : "))
                        t = float(input("Enter your t : "))
                        print("v = ", u + a * t)
                    except ValueError:
                        print("Invalid input.Please enter a valid number.")
                        continue
                    else:
                        break


            elif reaction == "u":
                while reaction == "u":
                    try:
                        v = float(input("Enter your v : "))
                        a = float(input("Enter your a : "))
                        t = float(input("Enter your t : "))
                        print("u = ", v - a * t)
                    except ValueError:
                        print("Invalid input.Please enter a valid number.")
                        continue
                    else:
                        break


            elif reaction == "a":
                while reaction == "a":
                    try:
                        u = float(input("Enter your u : "))
                        t = float(input("Enter your t : "))
                        v = float(input("Enter your v : "))
                        print("a = ", (v - u) / t)
                    except ValueError:
                        print("Invalid input.Please enter a valid number.")
                        continue
                    else:
                        break

            elif reaction == "t":
                while reaction == "t":
                    try:
                        v = float(input("Enter your v : "))
                        a = float(input("Enter your a : "))
                        u = float(input("Enter your u : "))
                        print("t = ", (v - u) / a)
                    except ValueError:
                        print("Invalid input.Please enter a valid number.")
                        continue
                    else:
                        break
        except ValueError:
            print("Error.Please enter a valid number")
            continue
        else:
            print("Thanks")
            break






