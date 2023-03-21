if __name__ == "__main__":
    try:
        celsius = float(input("Enter the temperature in Celsius: "))
        fahrenheit = (celsius * 1.8) + 32
        print(f"The temperature in Fahrenheit is:{fahrenheit}")
    except Exception as ex:
        print(f'log: {ex}')
