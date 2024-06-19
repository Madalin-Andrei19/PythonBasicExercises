"""
The input contains 1 integer, an operation +-*/ , and another integer. The output should contain the result of the expression. If the operation is not one of the +-/* , the program should print Unsupported operation. 
If the program encounters division by 0, it should print cannot divide by 0.
"""
a, s, b = int(input()), input(), int(input())
if s == "+":
    print(a+b)
elif s == "-":
    print(a-b)
elif s == "*":
    print(a*b)
elif s == "/":
    if b == 0:
        print("Cannot divide by 0")
    else: print(a/b)
else: print("Unsupported operation")
