x_value = int(input("enter the X value: "))
y_value = int(input("enter the Y value: "))
print("{:3}. Show the even numbers from {} to {}".format('i', x_value, y_value))
print("{:3}. Show the odd numbers from {} to {}".format('ii', x_value, y_value))
print("{:3}. Show the squares from {} to {}".format('iii', x_value, y_value))
print("{:3}. Exit the program".format('iv'))
choice = int(input(">>> "))
while choice != 4:
    if choice == 1:
        if x_value % 2 == 0:
            for i in range(x_value, y_value + 1, 2):
                print(i, end=' ')
        else:
            for i in range(x_value + 1, y_value + 1, 2):
                print(i, end=' ')
        choice = int(input("\n>>> "))
    elif choice == 2:
        if x_value % 2 != 0:
            for i in range(x_value, y_value + 1, 2):
                print(i, end=' ')
        else:
            for i in range(x_value+1, y_value+1,2):
                print(i, end=' ')
        choice = int(input("\n>>> "))
    elif choice == 3:
        print("square")
        for i in range(x_value,y_value+1):
            print(i*i, end=' ')
        choice = int(input("\n>>> "))
    else:
        print("incorrect choice. try again")
        choice = int(input(">>> "))
