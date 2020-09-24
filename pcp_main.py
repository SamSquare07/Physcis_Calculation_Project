from math import sqrt

def get_v():
    u = float(input("Enter your u : "))
    a = float(input("Enter your a : "))
    t = float(input("Enter your t : "))
    print("v = ", u + a*t)
#Formula 1


def get_u():

    v = float(input("Enter your v : "))
    a = float(input("Enter your a : "))
    t = float(input("Enter your t : "))
    print("u = ", v - a*t)
#Formula 1


def get_a():
    v = float(input("Enter your v : "))
    t = float(input("Enter your t : "))
    u = float(input("Enter your u : "))
    print("a = ", (v - u) / t)
#Formula 1


def get_t():
    u = float(input("Enter your u : "))
    a = float(input("Enter your a : "))
    v = float(input("Enter your v : "))
    print("t = ", (v - u) / a)
#Formula 1


def get_s():
    a = float(input("Enter your a : "))
    t = float(input("Enter your t : "))
    u = float(input("Enter your u : "))
    print(" s = ", u*t + 0.5*a*(t**2) )
#Formula 2


def get_u2():
    s = float(input("Enter your s : "))
    a = float(input("Enter your a : "))
    t = float(input("Enter your t : "))
    print(" u  = ", (s - 0.5*a*(t**2)) / t )
#Formula 2


def get_a2():
    s = float(input("Enter your s : "))
    u = float(input("Enter your u : "))
    t = float(input("Enter your t : "))
    print("a  = ", (2*s - 2*u*t) / t**2 )
#Formula 2


def get_t2():
    a = float(input("Enter your a : "))
    u = float(input("Enter your u : "))
    s = float(input("Enter your s : "))
    special_char = u ** 2 - 4 * 0.5 * a * -s
    ans = (-u + sqrt(special_char)) / (2 * (0.5 * a))
    print("t = ",ans)
#Formula 2


def get_v2():
    u = float(input("Enter your u : "))
    a = float(input("Enter your a : "))
    s = float(input("Enter your s : "))
    print(" v  = ",sqrt(u**2 + 2*a*s))
#Formula 3


def get_u3():
    v = float(input("Enter your v : "))
    a = float(input("Enter your a : "))
    s = float(input("Enter your s : "))
    print(" u  = ",sqrt(v**2 - 2*a*s))
#Formula 3


def get_s2():
    v = float(input("Enter your v : "))
    u = float(input("Enter your u : "))
    a = float(input("Enter your a : "))
    print("s = ",(v**2 - u**2)/2*a)
#Formula 3


def get_a3():
    v = float(input("Enter your v : "))
    u = float(input("Enter your u : "))
    s = float(input("Enter your s : "))
    print("a = ",(v**2 - u**2)/2*s )
#Formula 3
print("""Special note :
The formulas in this program assume that your object is being moved around on a flat surface with accelaration.
Trying to use it with any scenarios with deaccelaration or negative values will probably result in an error.

""")

while True:
    user_input_primary = input("""
Enter the number of the formula you want to use.
1.v = u + at.
2.s = ut + 0.5at^2
3.v^2 = u^2 + 2as

Your input : """) #primary input about the formula
    if user_input_primary == "1":
        user_input_secondary_1 = input("Enter your unknown value (v/u/a/t) : ")
        user_input_secondary_1 = user_input_secondary_1.lower() #eliminates the possibility of an uppercase letter ruining the ans
        if user_input_secondary_1 == "v" or user_input_secondary_1 == "u" or user_input_secondary_1 == "a" or user_input_secondary_1 == "t":
            if user_input_secondary_1 == "v":
                try:
                    get_v()
                    break
                except ValueError:
                    print("Error.Please try again with a valid input.")
                    continue

            elif user_input_secondary_1 == "u":
                try:
                    get_u()
                    break
                except ValueError:
                    print("Error.Please try again with a valid input.")
                    continue
            elif user_input_secondary_1 == "a":
                try:
                    get_a()
                    break
                except ValueError:
                    print("Error.Please try again with a valid input.")
                    continue
            elif user_input_secondary_1 == "t":
                try:
                    get_t()
                    break
                except ValueError:
                    print("Error.Please try again with a valid input.")
                    continue
        else:
            print("Error.Please try again with a valid input.")
            continue
    elif user_input_primary == "2":
        user_input_secondary_2 = input("Enter your unknown value (s/u/a/t) : ")
        user_input_secondary_2 = user_input_secondary_2.lower()
        if user_input_secondary_2 == "s" or user_input_secondary_2 == "u" or user_input_secondary_2 == "a" or user_input_secondary_2 == "t":
            if user_input_secondary_2 == "s":
                try:
                    get_s()
                    break
                except ValueError:
                    print("Error.Please try again with a valid input.")
                    continue
            elif user_input_secondary_2 == "u":
                try:
                    get_u2()
                    break
                except ValueError:
                    print("Error.Please try again with a valid input.")
                    continue
            elif user_input_secondary_2 == "a":
                try:
                    get_a()
                    break
                except ValueError:
                    print("Error.Please try again with a valid input.")
                    continue
            elif user_input_secondary_2 == "t":
                try:
                    get_t2()
                    break
                except ValueError:
                    print("Error.Please try again with a valid input.")
                    continue
        else:
            print("Error.Please try again with a valid input.")
            continue
    elif user_input_primary == "3":
        user_input_secondary_3 = input("Enter your unknown value (s/u/a/s) : ")
        user_input_secondary_3 = user_input_secondary_3.lower()
        if user_input_secondary_3 == "v" or user_input_secondary_3 == "u" or user_input_secondary_3 == "a" or user_input_secondary_3 == "s":
            if user_input_secondary_3 == "v":
                try:
                    get_v2()
                    break
                except ValueError:
                    print("Error.Please try again with a valid input.")
                    continue
            elif user_input_secondary_3 == "u":
                try:
                    get_u3()
                    break
                except ValueError:
                    print("Error.Please try again with a valid input.")
                    continue
            elif user_input_secondary_3 == "a":
                try:
                    get_a3()
                    break
                except ValueError:
                    print("Error.Please try again with a valid input.")
                    continue
            elif user_input_secondary_3 == "s":
                try:
                    get_s2()
                    break
                except ValueError:
                    print("Error.Please try again with a valid input.")
                    continue
        else:
            print("Error.Please try again with a valid input.")
            continue
    else:
        print("Error.Please try again with a valid input.")
        continue


exit_prompt = input("\nPress any key to exit the program ") #Only used to stop the program from abruptly shutting down in the .exe version








