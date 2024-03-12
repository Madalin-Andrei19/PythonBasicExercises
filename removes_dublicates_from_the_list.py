#1. set() method
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

set1 = set(my_list)
res_list = list(set1)
print("The list with unique elements only:")
print(res_list)

#2. list.append() and for loop
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
res_list = []

for item in my_list: 
    if item not in res_list: 
        res_list.append(item)
      
print("The list with unique elements only:")
print(res_list)
