def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) / 18

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = convert_fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit}°F = {celsius:.2f}°C")

