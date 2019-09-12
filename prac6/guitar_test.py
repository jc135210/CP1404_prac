from prac6.guitar import guitar


def main():
    my_guitars = []

    gibson = guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = guitar("Another Guitar", 2012, 500)
    print("expected 97. Got {}".format(gibson.get_age()))
    print("expected 7. Got {}".format(another_guitar.get_age()))
    print("expected True. Got {}".format(gibson.is_vintage()))
    print("expected False. Got {}".format(another_guitar.is_vintage())


main()
