a, b, c = int(input()), int(input()), int(input())
lst = sorted([a, b, c])
a = lst[0]
b = lst[1]
c = lst[2]
if (a**2) + (b**2) == c**2:
    print("RIGHT")
elif (a**2) + (b**2) > c**2:
    print("ACUTE")
elif (a**2) + (b**2) < c**2:
    print("OBTUSE")
