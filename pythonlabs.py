if __name__ == "__main__":
    try:
        num_1 = int(input('num_1 value: '))
        num_2 = int(input('num_2 value: '))
        print(f'res = {num_1 % num_2}', end ='')
        print(f'End!')
    except Exception as ex:
        print(f'log: {ex}')

#str = text
#int = iteger(3,344, 2432424, 3424, -123123)
#float = 4.545, 5.5646
#bool = 0[False], 1[True]
