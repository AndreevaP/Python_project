def pretty_print(mas):
    print('-' * 10)
    for row in mas:
        print(*row)
    print('-' * 10)

def get_number_from_index(i)
    print('1')

def get_empty_list(mas):
    for i in range(4):
        for j in range(4):
            if mas[i][j] == 0:
                print(i, j)


mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

mas[1][2] = 2
mas[3][0] = 4
get_empty_list(mas)
pretty_print(mas)
