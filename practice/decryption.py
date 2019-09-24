def main():
    letters_to_count = {}
    letters = load_file()
    for letter in letters:
        if letter in letters_to_count:
            letters_to_count[letter] += 1
        else:
            letters_to_count[letter] = 1
    load_file_1()


def load_file():
    """ opens a file and store the data as a list of list """
    word_lists = []
    special_char = ['.', '(', ')', ',', '-', ' ']
    code_file = open("code.txt", 'r')
    for line in code_file:
        coded_msg = line
        for char in special_char:
            coded_msg = coded_msg.replace(char, '')
        coded_msg = coded_msg.strip()
        word_lists.append(coded_msg)
    full_coded_msg = "".join(word_lists)
    code_file.close()
    return full_coded_msg


def load_file_1():
    """ opens a file and store the data as a list of list """
    word_lists = []
    special_char = ['.', '(', ')', ',', '-', ' ']
    encoded_file = open("code.txt", 'r')
    for line in encoded_file:
        coded_msg = line
        for char in coded_msg:
            if char == 't':
                coded_msg = coded_msg.replace(char, 'e')
            elif char == 'n':
                coded_msg = coded_msg.replace(char, 't')
            elif char == 'j':
                coded_msg = coded_msg.replace(char, 'r')
            elif char == 'x':
                coded_msg = coded_msg.replace(char, 'a')
            elif char == 'p':
                coded_msg = coded_msg.replace(char, 'i')
            elif char == 'i':
                coded_msg = coded_msg.replace(char, 'n')
        print(coded_msg)

    encoded_file.close()


main()
