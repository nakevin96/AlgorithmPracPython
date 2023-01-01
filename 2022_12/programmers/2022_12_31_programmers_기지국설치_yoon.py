import math


def solution(n, stations, w):
    result = 0
    check_list = []

    curr = 0
    for s in stations:
        s = s - 1
        left_end = max(0, s - w)
        right_end = min(n - 1, s + w)
        check_list.append((curr, left_end))
        curr = right_end + 1

    if curr < n:
        check_list.append((curr, n))

    divider = (2 * w) + 1
    for c0, c1 in check_list:
        result = result + math.ceil(((c1 - c0) / divider))
    return result

