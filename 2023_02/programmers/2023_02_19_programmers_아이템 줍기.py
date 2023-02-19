def solution(rectangle, c_x, c_y, itemX, itemY):
    from collections import deque
    queue = deque([[c_x, c_y]])
    result = 0
    
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    
    path = [[0 for _ in range(102)] for _ in range(102)]
    
    for rec in rectangle:
        for i in range(4):
            rec[i] = rec[i] * 2
        left_down, right_up = [rec[0], rec[1]], [rec[2], rec[3]]
        left_up, right_down = [rec[0], rec[3]], [rec[2], rec[1]]
        
        for i in range(left_down[1], left_up[1] + 1):
            if path[left_down[0]][i] == -1:
                continue
            path[left_down[0]][i] = 1
        for i in range(right_down[1], right_up[1] + 1):
            if path[right_down[0]][i] == -1:
                continue
            path[right_down[0]][i] = 1
        for i in range(left_up[0], right_up[0] + 1):
            if path[i][left_up[1]] == -1:
                continue
            path[i][left_up[1]] = 1
        for i in range(left_down[0], right_down[0] + 1):
            if path[i][left_down[1]] == -1:
                continue
            path[i][left_down[1]] = 1
        
        for i in range(left_down[1] + 1, left_up[1]):
            for j in range(left_down[0] + 1, right_down[0]):
                path[i][j] = -1
    
    while queue:
        cur_x, cur_y = queue.popleft()
        result += 1
        if cur_x == itemX and cur_y == itemY:
            return result // 2 - 1
        
        for i in range(4):
            n_x, n_y = dx[i] + cur_x, dy[i] + cur_y
            if (n_x, n_y) not in path:
                continue
            queue.append((n_x, n_y))
        
    return result // 2 - 1