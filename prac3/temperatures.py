"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            # fahrenheit = calculate_fahrenheit(celsius)
            print("Result: {:.2f} F".format(calculate_fahrenheit(celsius)))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            # celsius = calculate_celsius(fahrenheit)
            print("Result: {:.2f} C".format(calculate_celsius(fahrenheit)))
        else:
            print("Invalid option")
            print(MENU)
            choice = input(">>> ").upper()
    print("Thank you.")


def calculate_celsius(temperature):
    return 5 / 9 * (temperature - 32)


def calculate_fahrenheit(temperature):
    return temperature * 9.0 / 5 + 32



main()
