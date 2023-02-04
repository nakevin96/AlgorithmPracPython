def solution(commands):
    from collections import deque, defaultdict

    def change_val_get_visited(start_r, start_c, target_value):
        visited = {(start_r, start_c)}
        table[start_r][start_c] = target_value
        queue = deque([(start_r, start_c)])
        while queue:
            cr, cc = queue.popleft()
            for nr, nc in links[(cr, cc)]:
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    table[nr][nc] = value
                    queue.append((nr, nc))
        return visited

    result = []
    table = [["EMPTY" for _c in range(50)] for _r in range(50)]
    links = defaultdict(set)

    for cmd in commands:
        cmd = cmd.split(" ")
        if cmd[0] == "UPDATE":
            # UPDATE r c value
            # (r, c) 위치 value설정
            if len(cmd) == 4:
                r, c, value = int(cmd[1]) - 1, int(cmd[2]) - 1, cmd[3]
                change_val_get_visited(r, c, value)

            # UPDATE value1 value2
            # value1 값을 갖는 모든 셀들의 값을 value2로 변경
            else:
                value1, value2 = cmd[1], cmd[2]
                for sr in range(50):
                    for sc in range(50):
                        if value1 == table[sr][sc]:
                            table[sr][sc] = value2

        elif cmd[0] == "MERGE":
            # MERGE r1 c1 r2 c2
            # (r1, c1) (r2, c2)합치기
            r1, c1, r2, c2 = int(cmd[1]) - 1, int(cmd[2]) - 1, int(cmd[3]) - 1, int(cmd[4]) - 1
            if r1 == r2 and c1 == c2:
                continue

            links[(r1, c1)].add((r2, c2))
            links[(r2, c2)].add((r1, c1))
            value = table[r1][c1] if table[r1][c1] != "EMPTY" else table[r2][c2]

            if value != "EMPTY":
                change_val_get_visited(r1, c1, value)

        elif cmd[0] == "UNMERGE":
            # UNMERGE r c
            # r, c와 연결된 모든 셀을 초기 세팅으로
            r, c, value = int(cmd[1]) - 1, int(cmd[2]) - 1, "EMPTY"
            original_value = table[r][c]
            visited_set = change_val_get_visited(r, c, value)
            for vr, vc in visited_set:
                links[(vr, vc)].clear()
            table[r][c] = original_value

        elif cmd[0] == "PRINT":
            # PRINT r c
            # 비어있으면 "EMPTY" 아니면 값출력
            result.append(table[int(cmd[1]) - 1][int(cmd[2]) - 1])
    return result
