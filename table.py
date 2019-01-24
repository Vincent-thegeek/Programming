def top_line():
    print('+-----+------+')


def stand(n):
    for i in range(n):
        print('|    ', '|     ', '|     ')


def table():
    top_line()
    stand(4)
    top_line()
    stand(4)
    top_line()


table()
