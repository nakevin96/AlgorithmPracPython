"""
js풀이
function solution(n, edge) {
    const edgeMap = {};
    for (const vertices of edge){
        if (!(vertices[0] in edgeMap)) edgeMap[vertices[0]] = [];
        if (!(vertices[1] in edgeMap)) edgeMap[vertices[1]] = [];
        edgeMap[vertices[0]].push(vertices[1]);
        edgeMap[vertices[1]].push(vertices[0]);
    }

    const queue = [[1,0]];
    const visited = Array.from({length:n}, ()=>0);
    const result_list = [];
    let max_count = -1;
    while(queue.length){
        const [curr_vertex, curr_count] = queue.shift();
        if(visited[curr_vertex-1] === 0){
            visited[curr_vertex-1] = 1;
            result_list.push(curr_count);
            max_count = Math.max(max_count, curr_count)
            for(const next_vertex of edgeMap[curr_vertex]){
                if(visited[next_vertex-1] ===0){
                    queue.push([next_vertex, curr_count+1]);
                }
            }
        }
    }
    return result_list.filter((item)=>item===max_count).length
}
"""


def solution(n, edge):
    from collections import defaultdict
    from collections import deque
    vertex_map = defaultdict(list)

    for v1, v2 in edge:
        vertex_map[v1].append(v2)
        vertex_map[v2].append(v1)

    queue = deque([(1, 0)])
    visited = [0 for _ in range(n)]
    result = []

    while queue:
        curr_vertex, curr_count = queue.popleft()
        if visited[curr_vertex - 1] == 0:
            visited[curr_vertex - 1] = 1
            result.append((curr_vertex, curr_count))
            for next_vertex in vertex_map[curr_vertex]:
                if visited[next_vertex - 1] == 0:
                    queue.append((next_vertex, curr_count + 1))

    result.sort(key=lambda x: x[1])

    result_count = 0
    check_val = result[-1][1]
    while result[-1][1] == check_val:
        result_count += 1
        result.pop()
    return result_count
