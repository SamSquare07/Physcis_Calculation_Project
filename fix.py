def get_v():
    u = float(input("Enter your u : "))
    a = float(input("Enter your a : "))
    t = float(input("Enter your t : "))
    print("v = ", u + a*t)

def get_u():
    v = float(input("Enter your v : "))
    a = float(input("Enter your a : "))
    t = float(input("Enter your t : "))
    print("u = ", v - a*t)

def get_a():
    v = float(input("Enter your v : "))
    t = float(input("Enter your t : "))
    u = float(input("Enter your u : "))
    a = print("a = ", (v - u) / t)

def get_t():
    u = float(input("Enter your u : "))
    a = float(input("Enter your a : "))
    v = float(input("Enter your v : "))
    t = print("t = ", (v - u) / a)
    #These are the functions that hold the actual processes



while True:
    user_input = input("Enter your unknown value (v/u/a/t) : ")
    user_input = user_input.lower() #eliminating the possibility of an uppercase character
    if user_input == "v" or user_input == "u" or user_input == "a" or user_input == "t":
        if user_input == "v":
            try:
                get_v()
                break
            except ValueError:
                continue
        elif user_input == "u":
            try:
                get_u()
                break
            except ValueError:
                continue
        elif user_input == "a":
            try:
                get_a()
                break
            except ValueError:
                continue
        elif user_input == "t":
            try:
                get_t()
                break
            except ValueError:
                continue
    else:
        continue
#this code can work without all the while and ifs
#but I wanted to make it so that if a value is invalid,it keeps asking till it has the correct value


