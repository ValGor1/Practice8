max = 0
count_friends = 0
while True:
    N = int(input())
    if N>max:
        max = N
    if N == -1:
        break
    count_friends += 1
print(count_friends)
