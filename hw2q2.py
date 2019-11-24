def check_date_validity(date: str):
    d = [int(x) for x in date.split('/')]
    if d[0] < 1 or d[0] > 31 or d[1] < 1 or d[1] > 12 or d[2] < 1 or d[2] > 9999:
        return False
    if d[1] not in [1, 3, 5, 7, 8, 10, 12] and d[1] > 30:
        return False
    if not (d[1] == 2 and 30 > d[0] > 28 and d[2] % 4 == 0 and d[2] % 100 != 0 and d[2] % 400 == 0):
        return False
    else:
        return True


def date_finder(date: str, distance: int):
    d = [int(x) for x in date.split('/')]
    for i in range(0, abs(distance)):
        if distance < 0:
            if d[0] > 1:
                d[0] = d[0] -1
            elif d[2] > 1:
                if d[1] == 3 and ((d[2] % 4 == 0 and d[2] % 100 != 0) or d[2] % 400 == 0):
                    d[0] = 29
                elif d[1] == 3:
                    d[0] = 28
                if d[1] in [5, 7, 10, 12]:
                    d[0] = 30
                if d[1] in [1, 2, 4, 6, 8, 9, 11]:
                    d[0] = 31
                if d[1] > 1:
                    d[1] = d[1] - 1
                else:
                    d[1] = 12
                    d[2] = d[2] - 1
        else:
            if d[0] <= 27:
                d[0] = d[0] + 1
            elif d[1] != 2 and d[0] <= 29:
                d[0] = d[0] + 1
            elif d[0] == 28 and d[1] == 2 and ((d[2] % 4 == 0 and d[2] % 100 != 0) or d[2] % 400 == 0):
                d[0] = d[0] + 1
            elif d[0] == 30 and d[1] in [1, 3, 5, 7, 8, 10, 12]:
                d[0] = d[0] + 1
            else:
                if d[1] == 12 and d[0] == 31:
                    d[0] = 1
                    d[1] = 1
                    d[2] = d[2] + 1
                else:
                    d[0] = 1
                    d[1] = d[1] + 1
    print('{}/{}/{}'.format(d[0], d[1], d[2]))


print('Enter a date:')
date = str(input())
print('Enter number of days:')
distance = int(input())
date_finder(date, distance)