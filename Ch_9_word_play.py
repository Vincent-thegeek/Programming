def more_than():
    f = open('words.txt')
    for line in f:
        length = len(line.strip())
        if length > 15:
            print(line.strip())


def have_no_e(word):
    if 'e' in word or 'E' in word:
        print("There is an e in this word")
        return
    print("There is no E in this word")


def avoids(word, string):
    for i in string:
        if i in word:
            print("This word contains forbidden characters")
            return
    print("No forbidden characters")


def uses_only(word, characters):
    for i in word:
        if i not in characters:
            print("This word contains inappropriate characters")
            return
    print("This word contains the appropriate characters")


def us_only(word, characters):
    for i in characters:
        if i not in word:
            print("This word contains inappropriate characters")
            return
    print("This word contains the appropriate characters")


def is_abecederian(word):
    previous = word[0]
    for c in word:
        if c < previous:
            print("False")
            return
        previous = c
    print("True")


