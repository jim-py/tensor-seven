def check_password(password):
    if len(password) < 8:
        return 'Пароль меньше восьми символов!'
    elif 'password' in password.lower():
        return 'Пароль содержит слово password!'
    elif not any(map(str.isdigit, password)):
        return 'Пароль состоит только из букв!'
    elif not any(map(str.isalpha, password)):
        return 'Пароль состоит только из цифр!'
    return 'Пароль подходящий!'

def summa(*args):
    try:
        return f'Сумма чисел равна {sum(list(map(float, args[0].split())))}'
    except ValueError:
        return 'Должны быть только числа!'
