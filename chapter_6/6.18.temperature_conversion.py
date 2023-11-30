def temperature_conversion():
    print(f"1] fahrenheit -> celsius\n2] celsius -> fahrenheit ")
    mode_conversion = int(input("Choose the conversion mode : "))
    end = False
    while not end:
        if mode_conversion != 1 and mode_conversion != 2:
            return "Invalid Value"
            end=True
        elif mode_conversion == 1:
            print("You choose fahrenheit -> celsius")
            t_fahrenheit = float(input("Enter the temperature in fahrenheit : "))
            return f"{t_fahrenheit} fahrenheit is {round((t_fahrenheit - 32) / 1.8,3)} celsius"
        elif mode_conversion == 2:
            print("You choose celsius -> fahrenheit")
            t_celsius = float(input("Enter the temperature in Celsius : "))
            return f"{t_celsius}° Celsius is {t_celsius * 1.8 + 32} fahrenheit"
        else:
            return 'Enter a valid number'
print(temperature_conversion())

