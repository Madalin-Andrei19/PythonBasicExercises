"""
Task
The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:

1.The first line contains the sum of the two numbers.
2.The second line contains the difference of the two numbers (first - second).
3.The third line contains the product of the two numbers.
"""
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    sum_result = a + b
    difference_result = a - b
    product_result = a * b
    print(sum_result)
    print(difference_result)
    print(product_result)
