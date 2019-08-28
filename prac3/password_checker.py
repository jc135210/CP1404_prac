def oldpassword():
    MIN_LENGTH = 5
    password = input("enter password min length of {}".format(MIN_LENGTH))
    while len(password) > MIN_LENGTH:
        print("try again")
        password = input("enter password min length of {}".format(MIN_LENGTH))
    print('*' * len(password))


def main():
    MIN_LENGTH = 6
    password = get_password(MIN_LENGTH)
    display_astrix(password)


def get_password(length):
    password = input("enter password min length of {}".format(length))
    while len(password) > length:
        print("try again")
        password = input("enter password min length of {}".format(length))
    return password


def display_astrix(password):
    print('*' * len(password))
