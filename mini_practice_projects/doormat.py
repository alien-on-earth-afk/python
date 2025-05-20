r, c = map(int, input().split())

for i in range(r):
    if i < r // 2:
        pattern = '.|.' * (2 * i + 1)
    elif i == r // 2:
        pattern = 'WELCOME'
    else:
        pattern = '.|.' * (2 * (r - i - 1) + 1)
    
    print(pattern.center(c, '-'))
 