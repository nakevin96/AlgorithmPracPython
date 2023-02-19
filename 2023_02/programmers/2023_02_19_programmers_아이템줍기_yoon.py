def solution(rectangle, characterX, characterY, itemX, itemY):
    from collections import deque
    max_x, max_y = 0, 0
    for x1, y1, x2, y2 in rectangle:
        max_x = max(max_x, x1 * 2, x2 * 2)
        max_y = max(max_y, y1 * 2, y2 * 2)

    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    map_info = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    visited = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2
        min_r, max_r = min(y1, y2), max(y1, y2)
        min_c, max_c = min(x1, x2), max(x1, x2)
        for r in range(min_r, max_r + 1):
            if map_info[r][min_c] == 0:
                map_info[r][min_c] = 1
            if map_info[r][max_c] == 0:
                map_info[r][max_c] = 1
        for c in range(min_c, max_c + 1):
            if map_info[min_r][c] == 0:
                map_info[min_r][c] = 1
            if map_info[max_r][c] == 0:
                map_info[max_r][c] = 1
        for r in range(min_r + 1, max_r):
            for c in range(min_c + 1, max_c):
                map_info[r][c] = -1
    queue = deque([(characterY * 2, characterX * 2, 0)])
    visited[characterY*2][characterX*2] = 1
    while queue:
        cr, cc, step = queue.popleft()
        if cr == itemY * 2 and cc == itemX * 2:
            return step // 2
        for di in range(4):
            nr, nc = cr + direction[di][0], cc + direction[di][1]
            if nr < 0 or nc < 0 or nr > max_y or nc > max_x:
                continue
            if visited[nr][nc] == 0 and map_info[nr][nc] == 1:
                visited[nr][nc] = 1
                queue.append((nr, nc, step + 1))


print(solution([[1, 1, 2, 6], [3, 1, 4, 6], [0, 2, 5, 3], [0, 4, 5, 5]], 2, 2, 4, 4))
