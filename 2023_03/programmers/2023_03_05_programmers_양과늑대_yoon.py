# def solution(info, edges):
#     result = []
#
#     def check_node(sheep_count, wolf_count):
#         if sheep_count <= wolf_count:
#             return
#         result.append(sheep_count)
#         for source, target in edges:
#             if source in visited_set and target not in visited_set:
#                 is_sheep = True if info[target] == 0 else False
#                 visited_set.add(target)
#                 if is_sheep:
#                     check_node(sheep_count + 1, wolf_count)
#                 else:
#                     check_node(sheep_count, wolf_count + 1)
#                 visited_set.remove(target)
#
#     visited_set = {0}
#     check_node(1, 0)
#     return max(result)

# 처음에 풀려고 했던 방식으로 다시 풀어보기
def solution(info, edges):
    result = 0
    node_info = [[] for _ in range(len(info))]
    for source, target in edges:
        node_info[source].append(target)

    def check_node(sheep_count, wolf_count):
        nonlocal result
        if sheep_count <= wolf_count:
            return
        result = max(result, sheep_count)
        check_nodes = list(visited_set)
        for source_node in check_nodes:
            for next_node in node_info[source_node]:
                if next_node not in visited_set:
                    visited_set.add(next_node)
                    is_sheep = True if info[next_node] == 0 else False
                    if is_sheep:
                        check_node(sheep_count + 1, wolf_count)
                    else:
                        check_node(sheep_count, wolf_count + 1)
                    visited_set.remove(next_node)

    visited_set = {0}
    check_node(1, 0)
    return result
