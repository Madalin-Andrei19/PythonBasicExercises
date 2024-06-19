"""
Our task is to automate part of that process and print the resulting color after mixing any red, green, and blue colors.
Mixing red and blue results in purple.
Mixing red and ‘green results in yellow.
Mixing green and blue results in cyan.
The program gets as an input 2 colors that the designer wants to mix. Sometimes they make typos or input invalid colors - in that case, the program should print Invalid color. Otherwise, the program should print the result of the mix.
"""
c1, c2 = input(), input()

if c1 == "red":
    if c2 == "red":
        print("red")
    elif c2 == "blue":
        print("purple")
    elif c2 == "green":
        print("yellow")
    else: print("Invalid color")
      
elif c1 == "green":
    if c2 == "green":
        print("green")
    elif c2 == "blue":
        print("cyan")
    elif c2 == "red":
        print("yellow")
    else: print("Invalid color")
      
elif c1 == "blue":
    if c2 == "blue":
        print("blue")
    elif c2 == "red":
        print("purple")
    elif c2 == "green":
        print("cyan")
    else: print("Invalid color")
else: print("Invalid color")
