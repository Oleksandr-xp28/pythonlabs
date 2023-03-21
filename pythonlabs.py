
try:
    number = int(input('number->'))
    print(int(number/10))
    print(number%10)
except Exception as ex:
    print(f'log: {ex}')


