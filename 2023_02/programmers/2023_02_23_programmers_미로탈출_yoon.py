def solution(maps):
    from collections import deque
    r_len, c_len = len(maps), len(maps[0])
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    stop_over_list = [(0, 0), (0, 0), (0, 0)]
    count = 0
    for r in range(r_len):
        if count == 3:
            break
        for c in range(c_len):
            if maps[r][c] == 'S':
                stop_over_list[0] = (r, c)
                count += 1
            elif maps[r][c] == 'L':
                stop_over_list[1] = (r, c)
                count += 1
            elif maps[r][c] == 'E':
                stop_over_list[2] = (r, c)
                count += 1
            if count == 3:
                break

    def bfs(start, end):
        visited = [[0 for _c in range(c_len)] for _r in range(r_len)]
        queue = deque([(start[0], start[1], 0)])
        visited[start[0]][start[1]] = 1
        while queue:
            cr, cc, ct = queue.popleft()
            if cr == end[0] and cc == end[1]:
                return ct
            for di in range(4):
                nr, nc = cr + direction[di][0], cc + direction[di][1]
                if nr < 0 or nc < 0 or nr >= r_len or nc >= c_len:
                    continue
                if visited[nr][nc] == 0 and (maps[nr][nc] != 'X'):
                    visited[nr][nc] = 1
                    queue.append((nr, nc, ct + 1))
        return -1

    start_to_lever_time = bfs(stop_over_list[0], stop_over_list[1])
    if start_to_lever_time == -1:
        return -1
    lever_to_end_time = bfs(stop_over_list[1], stop_over_list[2])
    if lever_to_end_time == -1:
        return -1
    return start_to_lever_time + lever_to_end_time
