from math import *
from itertools import combinations

a = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
     ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
     ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
     ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
     ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]


def man_dis(x, y):
    return sum(abs(a - b) for a, b in zip(x, y))


def fun1(room: list) -> list:
    room_place = []
    for i in room:
        room_place.append((list(i)))
    return room_place

def fun2(re_places):
    list_P = []
    for i in range(5):
        for j in range(5):
            if re_places[i][j] == 'P':
                list_P.append([i, j])

    for x, y in combinations(list_P, 2):
        if man_dis(x, y) == 1:
            return 0
        elif man_dis(x, y) == 2:
            if x[0] == y[0]:  # x = 2,0 y = 2,2
                if re_places[x[0]][(x[1] + y[1]) // 2] == 'X':
                    continue
                else:
                    return 0
            elif x[1] == y[1]:
                if re_places[(x[0] + y[0]) // 2][x[1]] == 'X':
                    continue
                else:
                    return 0
            else:
                if re_places[x[0]][y[1]] == 'O' or re_places[y[0]][x[1]] == 'O':
                    return 0
    return 1

def solution(places):
    result = []
    for place in places:
        result.append(fun2(fun1(place)))
    return result

# print(solution(a))
