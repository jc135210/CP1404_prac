# Q1
OUTPUT_FILE = 'names.txt'
out_file = open(OUTPUT_FILE, 'w')
person_name = input('please enter your name: ')
print(person_name, file=out_file)
out_file.close()

# Q2
input_file = open(OUTPUT_FILE, 'r')
person_name = input_file.read().strip()
input_file.close()
print('Your name is: {}'.format(person_name))

# Q3
number_file = open('numbers.txt', 'r')
number_one = int(number_file.readline())
number_two = int(number_file.readline())
total = number_one + number_two
print(total)
number_file.close()

# Q4
total = 0
number_file = open('numbers2.txt', 'r')
for line in number_file:
    number = int(line)
    total += number
number_file.close()
print('the total is: ', total)
