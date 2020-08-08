import math
a = float(input("Enter your a : "))
u = float(input("Enter your u : "))
s = float(input("Enter your s : "))
special_char = u**2 - 4*0.5*a*-s
ans = (-u + math.sqrt(special_char)) / (2*(0.5*a))

print(ans)
