import numpy

a = numpy.random.randint(0, 100, size = (3, 3))
print('Матрица 3 на 3:')
for line in a:
    print(line)
print('\nТранспонированная матрица 3 на 3:')
for line in a.T:
    print(line)
