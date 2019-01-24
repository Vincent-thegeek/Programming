def crunch(word1, word2, ):
    for i in word1:
        for j in word2:
            print(i+j, end='    ')


def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1


def find2(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1


def counter(string, letter):
    count = 0
    print('Character', 'Count', sep="     ")
    for char in string:
        if char == letter:
            count = count + 1
        print(char, count, sep="             ")


def counter2(string, letter, index):
    count = 0
    print('Character', 'Count', sep="     ")
    while index < len(string):
        s = string[index]
        if string[index] == letter:
            count = count + 1
        print(s, count, sep='             ')
        index = index + 1


def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter, end="     ")


def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2)-1

    while j > 0:
        if word1[i] != word2[j]:
            return False
        i = i+1
        j = j-1

    print("Yo!!!")


def rotate_word(stri, number):
    b = []
    for k in range(len(stri)):
        a = ord(stri[k])
        a += number
        b.append(a)

    d = []
    for l in b:
        c = chr(l)
        d.append(c)
    e = "".join(d)
    print(e)


