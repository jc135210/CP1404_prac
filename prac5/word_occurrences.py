words_to_count = {}

user_text = input("Text: ")
words = user_text.split(" ")
for word in words:
    try:
        words_to_count[word] += 1
    except KeyError:
        words_to_count[word] = 1

for key, value in words_to_count.items():
    print("{:} : {}".format(key, value))

print("sorted printout\n")
words = list(words_to_count.keys())
words.sort()
max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, words_to_count[word]))
