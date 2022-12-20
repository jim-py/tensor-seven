from faker import Faker

fake = Faker('ru-RU')

pip_list_global_env = '''---Глобальное окружение---
pip                22.3.1
pycodestyle        2.10.0
PyQt5              5.15.7
PyQt5-Qt5          5.15.2
PyQt5-sip          12.11.0
python-dateutil    2.8.2
setuptools         63.2.0
six                1.16.0
sqlparse           0.4.3
tomli              2.0.1
tzdata             2022.4
yarl               1.8.1'''

pip_list_virtual_env = '''---Виртуальное окружение---
Faker           15.3.4
pip             22.3.1
python-dateutil 2.8.2
setuptools      63.2.0
six             1.16.0'''

print(f'ФИО: {fake.last_name_male()} {fake.first_name_male()} {fake.middle_name_male()}')

print(pip_list_global_env)
print(pip_list_virtual_env)
