# def solution(sequence):
#     # dp[0] => +, dp[1] => -
#     dp = [[0 for _ in range(len(sequence))] for _ in range(2)]
#     dp[0][0] = sequence[0]
#     dp[1][0] = -1 * sequence[0]
#
#     for s_idx in range(1, len(sequence)):
#         dp[0][s_idx] = max(sequence[s_idx], dp[1][s_idx - 1] + sequence[s_idx])
#         dp[1][s_idx] = max(-1 * sequence[s_idx], dp[0][s_idx - 1] - sequence[s_idx])
#
#     plus_max = max(dp[0])
#     minus_max = max(dp[1])
#     return max(plus_max, minus_max)

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