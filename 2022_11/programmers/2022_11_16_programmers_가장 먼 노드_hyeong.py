# https://school.programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque, defaultdict
import math

def solution(n, edge):
    path = defaultdict(list)
    
    for a, b in edge:
        path[a].append(b)
        path[b].append(a)
    
    far = {x:math.inf for x in range(1, n + 1)}
    
    far[1] = 1
    queue = deque([1])
    
    while queue:
        cur_node = queue.popleft()
        cur_far = far[cur_node]
        for i in path[cur_node]:
            if cur_far + 1 < far[i]:
                far[i] = cur_far + 1
                queue.append(i)
    
    return list(far.values()).count(max(far.values()))

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))