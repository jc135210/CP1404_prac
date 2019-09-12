from prac6.guitar import guitar


def main():
    my_guitars = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar_added = guitar(name, year, cost)
        my_guitars.append(guitar_added)
        print("{} added".format(guitar_added))
        name = input("Name: ")

    print("These are my guitars:")
    for i, item in enumerate(my_guitars):
        vintage_string = ""
        if item.is_vintage():
            vintage_string = '(vintage)'
        print("Guitar {}: {} ({}), worth ${:.2f} {}".format(i + 1, item.name, item.year, item.cost, vintage_string))


main()
