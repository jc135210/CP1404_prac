def main():
    type_of_ticket = get_type_ticket()
    destination = get_destination()


type_of_ticket = input("round Trip or return: ")
destinations = ["cairns", "sydney", "perth"]
destination = input("Enter your destination: ")
while destination not in destinations:
    destination = input("Enter your destination: (cairns, sydney, perth)")


def get_type_ticket():
    ticket_types = ['one way', 'return']
    ticket = input("one way or Return").lower()
    if ticket not in ticket_types:
        ticket = input("one way or return")
    if ticket == 'one way':
        return True
    else:
        return False


def get_destination():
    destinations = ["cairns", "sydney", "perth"]
    destination = input('Enter your destination: ({}) '.format(destinations))
    while destination not in destinations:
        destination = input('Enter your destination: ({}) '.format(destinations))
