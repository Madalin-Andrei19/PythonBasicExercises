"""
There are 3 types of triangles:
1. Equilateral: All 3 sides are equal
2.Isosceles: Only 2 sides are equal
3. Scalene: None of the sides are equal

!Note that a triangle is considered invalid if the sum of any two sides is less than or equal to the third side.
"""
a,b,c = int(input()), int(input()), int(input())
def type_of_triangle(a,b,c):
    if a + b <= c or a + c <= b or b + c <= a:
        print("Invalid triangle")
    elif a == b == c:
        print("Equilateral")
    elif a == b or a==c or b == c:
        print("Isosceles")
    else: print("Scalene")
type_of_triangle(a,b,c)
