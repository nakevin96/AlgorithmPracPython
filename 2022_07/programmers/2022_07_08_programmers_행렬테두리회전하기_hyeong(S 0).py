def solution(rows, columns, queries):
    result = []
    temp = [x for x in range(rows * columns + 1)]

    for quer in queries:
        index_list = []
        val_list = []
        left_top = (quer[0] - 1) * columns + quer[1]
        right_top = (quer[0] - 1) * columns + quer[3]
        left_bot = (quer[2] - 1) * columns + quer[1]
        right_bot = (quer[2] - 1) * columns + quer[3]

        index_list = [x for x in range(left_top, right_top)] + \
            [x for x in range(right_top, right_bot, columns)] + \
            [x for x in range(right_bot, left_bot, -1)] + \
            [x for x in range(left_top, left_bot, -columns)]

        val_list = [temp[i] for i in index_list]
        result.append(min(val_list))
        val_list.insert(0, val_list.pop())
        cnt = 0
        for i in index_list:
            temp[i] = val_list[cnt]
            cnt += 1

    return result

a = solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])
print(a)