def main():
    numbers = []
    for i in range(5):
        number = int(input('number: '))
        numbers.append(number)
    print('the first number is', numbers[0])
    print('the last number is', numbers[-1])
    print('the min number is', min(numbers))
    print('the max number is', max(numbers))
    print('avg of numbers is', sum(numbers) / len(numbers))

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'command', 'Execstate', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = input("enter your username: ")
    if username in usernames:
        print('access granted')
    else:
        print('access denied')


main()
