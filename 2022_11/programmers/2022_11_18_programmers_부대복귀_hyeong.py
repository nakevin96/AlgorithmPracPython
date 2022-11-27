# https://school.programmers.co.kr/learn/courses/30/lessons/132266

from collections import deque, defaultdict

def solution(n, roads, sources, destination):
    roads_path = defaultdict(list)
    for a, b in roads:
        roads_path[a].append(b)
        roads_path[b].append(a)
    
    queue = deque([destination])
    visited = {x:-1 for x in range(1, n+1)}
    visited[destination] = 0
    while queue:
        cur_road = queue.popleft()
        cur_dis = visited[cur_road]
        for nxt_road in roads_path[cur_road]:
            if visited[nxt_road] == -1:
                visited[nxt_road] = cur_dis + 1
                queue.append(nxt_road)
    return [visited[x] for x in sources]

'''
from collections import deque, defaultdict
import math

def solution(n, roads, sources, destination):
    roads_path = defaultdict(list)
    for a, b in roads:
        roads_path[a].append(b)
        roads_path[b].append(a)
    
    result = []
    for so in sources:
        queue = deque([so])
        visited = {x:math.inf for x in range(1, n + 1)}
        visited[so] = 0
        # x -> n ; value -> so 와의 거리
        while queue:
            if visited[destination] != math.inf:
                result.append(visited[destination])
                break
            cur_road = queue.popleft()
            cur_path = visited[cur_road]
            for next_road in roads_path[cur_road]:
                if visited[next_road] > cur_path + 1:
                    visited[next_road] = cur_path + 1
                    queue.append(next_road)
        if visited[destination] == math.inf:
            result.append(-1)
    return result
'''

'''
from collections import deque, defaultdict

def solution(n, roads, sources, destination):
    result = []
    roads_path = defaultdict(list)
    for a, b in roads:
        roads_path[a].append(b)
        roads_path[b].append(a)
    
    for so in sources:
        queue = deque([so])
        visited = {x:[-1, -1] for x in range(1, n+1)}
        visited[so] = [0, 0]
        # visited[road][0] -> 방문 여부
        # visited[road][1] -> 거리
        while queue:
            cur_road = queue.popleft()
            cur_path = visited[cur_road][1]
            # 거리
            if cur_road == destination:
                result.append(cur_path)
                break
            for nxt_road in roads_path[cur_road]:
                if visited[nxt_road][0] == -1:
                    # 방문 여부
                    queue.append(nxt_road)
                    visited[nxt_road] = [0, cur_path + 1]
        if visited[destination][0] == -1:
            result.append(-1)
    return result
                    
'''