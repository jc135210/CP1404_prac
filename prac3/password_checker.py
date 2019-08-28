MIN_LENGTH = 5

password = input("enter password min length of {}".format(MIN_LENGTH))
while len(password) > MIN_LENGTH:
    print("try again")
    password = input("enter password min length of {}".format(MIN_LENGTH))
print('*' * len(password))
