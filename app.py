check = 1
in_pass = input('Введите пароль:')
quanty = len(in_pass)


try:    
    passw = check/quanty
    passw2 = int(in_pass)
    print('Welcome')
except ZeroDivisionError:
    print('Вы ввели пустой пароль')
except ValueError:
    print('Ваш пароль содержит буквы')

