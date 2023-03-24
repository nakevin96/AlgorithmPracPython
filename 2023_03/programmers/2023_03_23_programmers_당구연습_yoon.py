# https://school.programmers.co.kr/learn/courses/30/lessons/169198
def solution(m, n, startX, startY, balls):
    result = []
    for x, y in balls:
        tmp_result = m ** 2 + n ** 2
        dx, dy = abs(startX - x), abs(startY - y)

        left_wall = ((startX + x) ** 2) + (dy ** 2)
        right_wall = ((2 * m - startX - x) ** 2) + (dy ** 2)
        top_wall = ((2 * n - startY - y) ** 2) + (dx ** 2)
        bottom_wall = ((startY + y) ** 2) + (dx ** 2)

        if dx == 0:
            if startY < y:
                tmp_result = min(tmp_result, left_wall, bottom_wall, right_wall)
            else:
                tmp_result = min(tmp_result, left_wall, top_wall, right_wall)

        elif dy == 0:
            if startX < x:
                tmp_result = min(tmp_result, left_wall, top_wall, bottom_wall)
            else:
                tmp_result = min(tmp_result, right_wall, top_wall, bottom_wall)

        else:
            tmp_result = min(tmp_result, left_wall, right_wall, top_wall, bottom_wall)
        result.append(tmp_result)

    return result
