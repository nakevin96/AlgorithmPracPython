def solution(n, roads, sources, destination):
    from collections import defaultdict
    from collections import deque
    map_info = defaultdict(list)

    for r1, r2 in roads:
        map_info[r1].append(r2)
        map_info[r2].append(r1)

    result = [-1 for _ in range(n + 1)]
    visited = [0 for _ in range(n + 1)]

    queue = deque([(destination, 0)])

    while queue:
        curr_place, curr_time = queue.popleft()
        if visited[curr_place] == 0:
            visited[curr_place] = 1
            result[curr_place] = curr_time
            for next_place in map_info[curr_place]:
                if visited[next_place] == 0:
                    queue.append((next_place, curr_time + 1))

    return [result[s] for s in sources]