from collections import deque


def solution(rows, columns, queries):
    map_info = [i for i in range((rows * columns) + 1)]
    result = []

    for query in queries:
        move_idx_list = list()
        left_top = (query[0] - 1) * columns + query[1]
        right_top = (query[0] - 1) * columns + query[3]
        right_bottom = (query[2] - 1) * columns + query[3]
        left_bottom = (query[2] - 1) * columns + query[1]
        move_idx_list.extend([n for n in range(left_top, right_top)])
        move_idx_list.extend([n for n in range(right_top, right_bottom, columns)])
        move_idx_list.extend([n for n in range(right_bottom, left_bottom, -1)])
        move_idx_list.extend([n for n in range(left_bottom, left_top, -columns)])

        value_list = deque([map_info[m_idx] for m_idx in move_idx_list])
        value_list.appendleft(value_list.pop())
        result.append(min(value_list))

        for _idx in range(len(move_idx_list)):
            map_info[move_idx_list[_idx]] = value_list[_idx]

    return result