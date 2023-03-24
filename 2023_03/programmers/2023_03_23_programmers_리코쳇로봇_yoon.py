# https://school.programmers.co.kr/learn/courses/30/lessons/169199
def solution(board):
    from collections import deque
    R, C = len(board), len(board[0])
    map_info = [[0 for _ in range(C)] for _ in range(R)]
    visited = [[0 for _ in range(C)] for _ in range(R)]
    start = []
    end = []

    for br in range(R):
        for bc in range(C):
            if board[br][bc] == 'D':
                map_info[br][bc] = 1
            elif board[br][bc] == 'R':
                start = [br, bc]
            elif board[br][bc] == 'G':
                end = [br, bc]

    queue = deque([(start[0], start[1], 0)])
    visited[start[0]][start[1]] = 1

    while queue:
        cr, cc, count = queue.popleft()
        # 상, 하, 좌 우 이동
        if cr == end[0] and cc == end[1]:
            return count

        right_r = cr
        while right_r + 1 < R and map_info[right_r + 1][cc] == 0:
            right_r += 1

        if right_r > cr and visited[right_r][cc] == 0:
            visited[right_r][cc] = 1
            queue.append((right_r, cc, count + 1))

        left_r = cr
        while left_r - 1 >= 0 and map_info[left_r - 1][cc] == 0:
            left_r -= 1

        if left_r < cr and visited[left_r][cc] == 0:
            visited[left_r][cc] = 1
            queue.append((left_r, cc, count + 1))

        top_c = cc
        while top_c - 1 >= 0 and map_info[cr][top_c - 1] == 0:
            top_c -= 1
        if top_c < cc and visited[cr][top_c] == 0:
            visited[cr][top_c] = 1
            queue.append((cr, top_c, count + 1))

        bottom_c = cc
        while bottom_c + 1 < C and map_info[cr][bottom_c + 1] == 0:
            bottom_c += 1
        if bottom_c > cc and visited[cr][bottom_c] == 0:
            visited[cr][bottom_c] = 1
            queue.append((cr, bottom_c, count + 1))
    return -1
