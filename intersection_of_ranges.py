"""Given two ranges your task is to find their intersection (the intersection range). The input contains 4 numbers:
the left and right endpoints of the first segment, and then the left and the right endpoints of the second segment.
If the ranges don't intersect, the program should print No intersection.
If the ranges have only a single common point, the program should output that number.
If the ranges have an overlap, the program should print the overlap (small number first, then the big one).
It's guaranteed that for each segment, the left and the right endpoints are not the same. """

a, b, c, d = int(input()), int(input()), int(input()), int(input())
list1 = []
list2 = []
for i in range(a, b+1):
    list1.append(i)
for j in range(c, d+1):
    list2.append(j)
lst3 = [value for value in list1 if value in list2]
if not lst3:
    print("No intersection")
else:
    if lst3[0] == lst3[-1]:
        print(lst3[0])
    else:
        print(lst3[0])
        print(lst3[-1])
