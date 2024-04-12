N = input('Введите число')
T = True
if N.isdigit() == True:
    print('Введено целое число:',N)
else:
    while T is True:
        N=input('Ошибка. Попробуйте еще раз.Введите число:')
        if N.isdigit() == True:
            print('Введено целое число:',N)
            T = False
            break