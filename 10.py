N = int(input())
count = 0
a = [6, 28, 496, 8128, 33550336, 137438691328]
for i in range(2, N+1):
    if i in a:
        print(i)

