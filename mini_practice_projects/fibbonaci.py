#a script for printing fibonacci series

n = int(input("Enter n: "))
fibo = 0
_sum = 1
for _ in range(n):
    print(fibo, end=" ")
    temp = fibo
    fibo = fibo + _sum
    _sum = temp

#0, 1, 1, 2, 3, 5, 8, 13