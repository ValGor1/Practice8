all_salary = 0
count_employees = 0
while True:
    N = int(input())
    if N == 0:
        break
    count_employees += 1
    all_salary += N
print(all_salary/count_employees)
