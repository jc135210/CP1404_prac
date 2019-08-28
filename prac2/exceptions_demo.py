try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator != 0:
        fraction = numerator / denominator
        print(fraction)
    else:
        print(" not possible")
except ValueError:
    print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#    print("Cannot divide by zero!")
print("Finished.")

# TODO remove the except ZeroDivision error
