#a script for printing fibonacci series

"""
n = int(input("Enter n: "))
fibo = 0
_sum = 1
for _ in range(n):
    print(fibo, end=" ")
    temp = fibo
    fibo = fibo + _sum
    _sum = temp
"""
# #^ working
# #0, 1, 1, 2, 3, 5, 8, 13

#recurrsion
def fibo(n):
    if (n==0 or n==1):
        return n
    return fibo(n-2) + fibo(n-1)

print(fibo(3))