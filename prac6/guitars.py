from prac6.guitar import Guitar


def main():
    my_guitars = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar_added = Guitar(name, year, cost)
        my_guitars.append(guitar_added)
        print("{} added".format(guitar_added))
        name = input("Name: ")

    print("These are my guitars:")
    for i, my_guitar in enumerate(my_guitars):
        vintage_string = ""
        if my_guitar.is_vintage():
            vintage_string = '(vintage)'
        print("Guitar {}: {} ({}), worth ${:.2f} {}".format(i + 1, my_guitar.name, my_guitar.year, my_guitar.cost,
                                                            vintage_string))


main()
