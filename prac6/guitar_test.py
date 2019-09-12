from prac6.guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2012, 500)
    print("expected 97. Got {}".format(gibson.get_age()))
    print("expected 7. Got {}".format(another_guitar.get_age()))
    print("expected True. Got {}".format(gibson.is_vintage()))
    print("expected False. Got {}".format(another_guitar.is_vintage()))


main()
