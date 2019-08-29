import random

MINIMUM = 1
MAXIMUM = 45


def main():
    number_quickpick = int(input('how many quick pick? '))
    while number_quickpick < 0:
        print("invalid number")
        number_quickpick = int(input('how many quick picks? '))

    for i in range(number_quickpick):
        quickpicks = []
        for x in range(6):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quickpicks:
                number = random.randint(MINIMUM, MAXIMUM)
            quickpicks.append(number)
        quickpicks.sort()
        print(' '.join('{:2}'.format(number) for number in quickpicks))


main()
