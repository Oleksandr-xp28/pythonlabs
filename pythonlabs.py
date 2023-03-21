
try:
    number = int(input('Enter a number: '))

    first_digit = int(number / 100)
    second_digit = int((number % 100) / 10)
    third_digit = number % 10

    print(first_digit)
    print(second_digit)
    print(third_digit)

    total = first_digit + second_digit + third_digit
    print(total)
except Exception as ex:
    print(f'log: {ex}')