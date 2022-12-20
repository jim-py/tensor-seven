import os

print(f'1. Имя операционной системы: {os.name}\n2. Имя пользователя: {os.getlogin()}\n3. Файлы и директории: {os.listdir()}')
